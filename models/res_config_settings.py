from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    use_s3_gallery = fields.Boolean(string="Usar Amazon S3 para galería")
    s3_access_key = fields.Char(string="S3 Access Key")
    s3_secret_key = fields.Char(string="S3 Secret Key")
    s3_bucket_name = fields.Char(string="S3 Bucket")
    s3_region = fields.Char(string="S3 Región")

    def set_values(self):
        super().set_values()
        config = self.env['ir.config_parameter'].sudo()
        config.set_param('gallery.use_s3', self.use_s3_gallery)
        config.set_param('gallery.s3_access_key', self.s3_access_key)
        config.set_param('gallery.s3_secret_key', self.s3_secret_key)
        config.set_param('gallery.s3_bucket_name', self.s3_bucket_name)
        config.set_param('gallery.s3_region', self.s3_region)

    def get_values(self):
        res = super().get_values()
        config = self.env['ir.config_parameter'].sudo()
        res.update(
            use_s3_gallery=config.get_param('gallery.use_s3') == 'True',
            s3_access_key=config.get_param('gallery.s3_access_key'),
            s3_secret_key=config.get_param('gallery.s3_secret_key'),
            s3_bucket_name=config.get_param('gallery.s3_bucket_name'),
            s3_region=config.get_param('gallery.s3_region'),
        )
        return res