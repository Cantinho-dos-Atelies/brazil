# Copyright 2023 Akretion - Raphaël Valyi <raphael.valyi@akretion.com>
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
# Generated by https://github.com/akretion/xsdata-odoo
#
import textwrap
from odoo import fields, models

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"

"Tipo do Componente"
COMP_TPCOMP = [
    ("01", "Vale Pedágio"),
    ("02", "Impostos, taxas e contribuições"),
    ("03", "Despesas (bancárias, meios de pagamento, outras)"),
    ("99", "Outros"),
]

"Descrição do Evento - “Pagamento Operação MDF-e”"
EVPAGTOOPERMDFE_DESCEVENTO = [
    ("Pagamento Operação MDF-e", "Pagamento Operação MDF-e"),
    ("Pagamento Operacao MDF-e", "Pagamento Operacao MDF-e"),
]

"Indicador da Forma de Pagamento"
INFPAG_INDPAG = [
    ("0", "Pagamento à Vista"),
    ("1", "Pagamento à Prazo"),
]


class EvPagtoOperMdfe(models.AbstractModel):
    """Schema XML de validação do evento de pagamento da operação de transporte
    110116"""

    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = "mdfe.30.evpagtoopermdfe"
    _inherit = "spec.mixin.mdfe"
    _binding_type = "EvPagtoOperMdfe"

    mdfe30_descEvento = fields.Selection(
        EVPAGTOOPERMDFE_DESCEVENTO,
        string="Descrição do Evento",
        xsd_required=True,
        help="Descrição do Evento - “Pagamento Operação MDF-e”",
    )

    mdfe30_nProt = fields.Char(
        string="Número do Protocolo de Status do MDF-e",
        xsd_required=True,
        xsd_type="TProt",
        help=(
            "Número do Protocolo de Status do MDF-e. \n1 posição tipo de "
            "autorizador (9 - SEFAZ Nacional ); \n2 posições ano;\n10 "
            "seqüencial no ano."
        ),
    )

    mdfe30_infViagens = fields.Many2one(
        comodel_name="mdfe.30.infviagens",
        string="Informações do total",
        xsd_required=True,
        help=(
            "Informações do total de viagens acobertadas pelo Evento "
            "“pagamento do frete”"
        ),
    )

    mdfe30_infPag = fields.One2many(
        "mdfe.30.evpagtoopermdfe_infpag",
        "mdfe30_infPag_evPagtoOperMDFe_id",
        string="Informações do Pagamento do Frete",
    )


class InfViagens(models.AbstractModel):
    """Informações do total de viagens acobertadas pelo Evento “pagamento do
    frete”"""

    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = "mdfe.30.infviagens"
    _inherit = "spec.mixin.mdfe"
    _binding_type = "EvPagtoOperMdfe.InfViagens"

    mdfe30_qtdViagens = fields.Char(
        string="Quantidade total",
        xsd_required=True,
        help=("Quantidade total de viagens realizadas com o pagamento do Frete"),
    )

    mdfe30_nroViagem = fields.Char(
        string="Número de referência da viagem",
        xsd_required=True,
        help="Número de referência da viagem do MDFe referenciado.",
    )


class EvPagtoOperMdfeInfPag(models.AbstractModel):
    "Informações do Pagamento do Frete"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = "mdfe.30.evpagtoopermdfe_infpag"
    _inherit = "spec.mixin.mdfe"
    _binding_type = "EvPagtoOperMdfe.InfPag"

    mdfe30_infPag_evPagtoOperMDFe_id = fields.Many2one(
        comodel_name="mdfe.30.evpagtoopermdfe", xsd_implicit=True, ondelete="cascade"
    )
    mdfe30_xNome = fields.Char(
        string="Razão social ou Nome do responsavel",
        help="Razão social ou Nome do responsavel pelo pagamento",
    )

    mdfe30_CPF = fields.Char(
        string="Número do CPF do responsável pelo pgto",
        choice="infpag",
        xsd_choice_required=True,
        xsd_type="TCpf",
        help=(
            "Número do CPF do responsável pelo pgto\nInformar os zeros não "
            "significativos."
        ),
    )

    mdfe30_CNPJ = fields.Char(
        string="Número do CNPJ do responsável pelo pgto",
        choice="infpag",
        xsd_choice_required=True,
        xsd_type="TCnpjOpc",
        help=(
            "Número do CNPJ do responsável pelo pgto\nInformar os zeros não "
            "significativos."
        ),
    )

    mdfe30_idEstrangeiro = fields.Char(
        string="Identificador do responsável pelo pgto",
        choice="infpag",
        xsd_choice_required=True,
        help=("Identificador do responsável pelo pgto em caso de ser estrangeiro"),
    )

    mdfe30_comp = fields.One2many(
        "mdfe.30.evpagtoopermdfe_comp",
        "mdfe30_Comp_infPag_id",
        string="Componentes do Pagamentoi do Frete",
    )

    mdfe30_vContrato = fields.Monetary(
        string="Valor Total do Contrato",
        xsd_required=True,
        xsd_type="TDec_1302",
        currency_field="brl_currency_id",
    )

    mdfe30_indPag = fields.Selection(
        INFPAG_INDPAG,
        string="Indicador da Forma",
        xsd_required=True,
        help=(
            "Indicador da Forma de Pagamento:0-Pagamento à Vista;1-Pagamento à"
            " Prazo;"
        ),
    )

    mdfe30_vAdiant = fields.Monetary(
        string="Valor do Adiantamento",
        xsd_type="TDec_1302",
        currency_field="brl_currency_id",
        help="Valor do Adiantamento (usar apenas em pagamento à Prazo",
    )

    mdfe30_infPrazo = fields.One2many(
        "mdfe.30.evpagtoopermdfe_infprazo",
        "mdfe30_infPrazo_infPag_id",
        string="Informações do pagamento a prazo",
        help=(
            "Informações do pagamento a prazo.\nInformar somente se indPag for"
            " à Prazo"
        ),
    )

    mdfe30_infBanc = fields.Many2one(
        comodel_name="mdfe.30.evpagtoopermdfe_infbanc",
        string="Informações bancárias",
        xsd_required=True,
    )


class EvPagtoOperMdfeComp(models.AbstractModel):
    "Componentes do Pagamentoi do Frete"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = "mdfe.30.evpagtoopermdfe_comp"
    _inherit = "spec.mixin.mdfe"
    _binding_type = "EvPagtoOperMdfe.InfPag.Comp"

    mdfe30_Comp_infPag_id = fields.Many2one(
        comodel_name="mdfe.30.evpagtoopermdfe_infpag",
        xsd_implicit=True,
        ondelete="cascade",
    )
    mdfe30_tpComp = fields.Selection(
        COMP_TPCOMP,
        string="Tipo do Componente",
        xsd_required=True,
        help=(
            "Tipo do Componente\n01 - Vale Pedágio; \n02 - Impostos, taxas e "
            "contribuições; \n03 - Despesas (bancárias, meios de pagamento, "
            "outras)\n; 99 - Outros"
        ),
    )

    mdfe30_vComp = fields.Monetary(
        string="Valor do componente",
        xsd_required=True,
        xsd_type="TDec_1302",
        currency_field="brl_currency_id",
    )

    mdfe30_xComp = fields.Char(string="Descrição do componente do tipo Outros")


class EvPagtoOperMdfeInfPrazo(models.AbstractModel):
    """Informações do pagamento a prazo.
    Informar somente se indPag for à Prazo"""

    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = "mdfe.30.evpagtoopermdfe_infprazo"
    _inherit = "spec.mixin.mdfe"
    _binding_type = "EvPagtoOperMdfe.InfPag.InfPrazo"

    mdfe30_infPrazo_infPag_id = fields.Many2one(
        comodel_name="mdfe.30.evpagtoopermdfe_infpag",
        xsd_implicit=True,
        ondelete="cascade",
    )
    mdfe30_nParcela = fields.Char(string="Número da Parcela", xsd_required=True)

    mdfe30_dVenc = fields.Date(
        string="Data de vencimento da Parcela",
        xsd_required=True,
        xsd_type="TData",
        help="Data de vencimento da Parcela (AAAA-MM-DD)",
    )

    mdfe30_vParcela = fields.Monetary(
        string="Valor da Parcela",
        xsd_required=True,
        xsd_type="TDec_1302Opc",
        currency_field="brl_currency_id",
    )


class EvPagtoOperMdfeInfBanc(models.AbstractModel):
    "Informações bancárias"
    _description = textwrap.dedent("    %s" % (__doc__,))
    _name = "mdfe.30.evpagtoopermdfe_infbanc"
    _inherit = "spec.mixin.mdfe"
    _binding_type = "EvPagtoOperMdfe.InfPag.InfBanc"

    mdfe30_codBanco = fields.Char(
        string="Número do banco", choice="infbanc", xsd_choice_required=True
    )

    mdfe30_codAgencia = fields.Char(
        string="Número da agência bancária", choice="infbanc", xsd_choice_required=True
    )

    mdfe30_CNPJIPEF = fields.Char(
        string="Número do CNPJ da Instituição",
        choice="infbanc",
        xsd_choice_required=True,
        xsd_type="TCnpjOpc",
        help=(
            "Número do CNPJ da Instituição de Pagamento Eletrônico do "
            "Frete\nInformar os zeros não significativos."
        ),
    )

    mdfe30_PIX = fields.Char(
        string="Chave PIX",
        choice="infbanc",
        xsd_choice_required=True,
        help=(
            "Chave PIX\nInformar a chave PIX para recebimento do frete. \nPode"
            " ser email, CPF/ CNPJ (somente numeros), Telefone com a seguinte "
            "formatação (+5599999999999) ou a chave aleatória gerada pela "
            "instituição."
        ),
    )
