import boto3
import base64
import uuid
from odoo import models, fields, api

class ProductImage(models.Model):
    _name = 'product.image.gallery'
    _description = 'Product Image Gallery'

    product_tmpl_id = fields.Many2one('product.template', string='Product')
    image = fields.Binary("Image", attachment=True)
    image_url = fields.Char("Image URL")
    name = fields.Char("Descripción")

    @api.model
    def create(self, vals):
        vals = self._handle_s3_upload(vals)
        return super().create(vals)

    def write(self, vals):
        vals = self._handle_s3_upload(vals)
        return super().write(vals)

    def _handle_s3_upload(self, vals):
        config = self.env['ir.config_parameter'].sudo()
        use_s3 = config.get_param('gallery.use_s3') == 'True'
        if use_s3 and 'image' in vals:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=config.get_param('gallery.s3_access_key'),
                aws_secret_access_key=config.get_param('gallery.s3_secret_key'),
                region_name=config.get_param('gallery.s3_region'),
            )
            bucket = config.get_param('gallery.s3_bucket_name')
            image_data = base64.b64decode(vals['image'])
            key = f"product_gallery/{uuid.uuid4().hex}.png"

            s3_client.put_object(Bucket=bucket, Key=key, Body=image_data, ContentType='image/png')
            vals['image_url'] = f"https://{bucket}.s3.{s3_client.meta.region_name}.amazonaws.com/{key}"
            vals.pop('image')

        return vals

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    gallery_image_ids = fields.One2many(
        'product.image.gallery', 'product_tmpl_id', string='Gallery Images'
    )