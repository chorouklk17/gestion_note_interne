from odoo import fields, models


class NotePartage(models.Model):
    _name = "note.partage"
    _description = "Note Partagée"

    name = fields.Char(string="Titre de la note", required=True)
    auteur = fields.Char(string="Auteur")
    date_creation = fields.Date(string="Date de création", default=fields.Date.context_today)
    statut = fields.Selection(
        [
            ("brouillon", "Brouillon"),
            ("partage", "Partagée"),
            ("termine", "Terminée"),
        ],
        string="Statut",
        default="brouillon",
    )
    contenu = fields.Html(string="Contenu de la note")
