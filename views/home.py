from fasthtml.common import *


def layout_login(error_message: str = None, success_message: str = None):
    feedback = None
    if error_message:
        feedback = P(error_message, style="color:#fda4af; margin-bottom:12px;")
    elif success_message:
        feedback = P(success_message, style="color:#86efac; margin-bottom:12px;")

    return (
        Header(
            H1("🚀 Espaço Viagem 🚀", style="text-align:center; margin-top:24px; color:#ffffff; font-size:clamp(24px, 4vw, 34px); text-shadow:0 0 12px rgba(125,211,252,0.6);"),
            style="background:linear-gradient(135deg, #020617, #2563eb 45%, #0ea5e9 100%); padding:24px 16px; border-bottom:3px solid #7dd3fc;"
        ),
        Main(
            Section(
                Div(
                    H2("Acesso ao portal", style="margin:0 0 8px; color:#f8fafc;"),
                    P("Entre para continuar sua viagem pelo cosmos.", style="margin:0 0 20px; color:#cbd5e1;"),
                    P("Usuário de teste: admin / senha: admin123", style="margin:0 0 16px; color:#7dd3fc; font-size:0.95rem;"),
                    feedback,
                    Form(
                        Label("Usuário", style="display:block; margin-bottom:6px; color:#e2e8f0;"),
                        Input(type="text", name="username", placeholder="Digite seu usuário", style="width:100%; padding:10px 12px; border-radius:8px; border:1px solid #475569; margin-bottom:12px;"),
                        Label("Senha", style="display:block; margin-bottom:6px; color:#e2e8f0;"),
                        Input(type="password", name="password", placeholder="Digite sua senha", style="width:100%; padding:10px 12px; border-radius:8px; border:1px solid #475569; margin-bottom:16px;"),
                        Button("Entrar", type="submit", style="width:100%; padding:10px 12px; border:none; border-radius:8px; background:#38bdf8; color:#0f172a; font-weight:bold; cursor:pointer; margin-bottom:10px;"),
                        action="/home",
                        method="get",
                        style="display:flex; flex-direction:column;"
                    ),
                    A("Criar conta", href="/cadastrar", style="display:block; margin-top:8px; color:#7dd3fc; text-align:center; text-decoration:none; font-weight:bold;"),
                    style="max-width:440px; margin:60px auto; padding:34px; border-radius:28px; background:linear-gradient(145deg, rgba(2, 6, 23, 0.98), rgba(37, 99, 235, 0.9)); box-shadow:0 25px 70px rgba(2, 6, 23, 0.6); border:2px solid rgba(125, 211, 252, 0.4);"
                ),
                style="min-height:70vh; background:radial-gradient(circle at top, #1d4ed8 0%, #020617 70%); padding:20px 0;"
            )
        ),
        Footer(
            P("© 2026 Projeto Espaço Viagem - Desenvolvido para estudos de programação e astronomia.", style="text-align:center; color:#cbd5e1; padding:20px 0;")
        )
    )


def layout_admin(users, error_message: str = None, success_message: str = None):
    feedback = None
    if error_message:
        feedback = P(error_message, style="color:#fda4af; margin-bottom:12px;")
    elif success_message:
        feedback = P(success_message, style="color:#86efac; margin-bottom:12px;")

    rows = []
    for user in users:
        rows.append(
            Tr(
                Td(str(user["id"])),
                Td(user["username"]),
                Td(
                    A("Apagar", href=f"/admin/delete/{user['id']}", style="color:#fda4af; font-weight:bold; text-decoration:none;")
                    if user["username"] != "admin" else ""
                ),
            )
        )

    return (
        Header(
            H1("🛠️ Painel administrativo", style="text-align:center; margin:0; color:#f8fafc;"),
            style="background:linear-gradient(135deg, #020617, #2563eb); padding:24px 20px;"
        ),
        Main(
            Section(
                Div(
                    H2("Gerenciar usuários", style="margin:0 0 8px; color:#f8fafc;"),
                    P("Crie novos usuários ou remova os cadastrados.", style="margin:0 0 16px; color:#cbd5e1;"),
                    feedback,
                    Form(
                        Label("Usuário", style="display:block; margin-bottom:6px; color:#e2e8f0;"),
                        Input(type="text", name="username", placeholder="Nome do usuário", style="width:100%; padding:10px 12px; border-radius:8px; border:1px solid #475569; margin-bottom:12px;"),
                        Label("Senha", style="display:block; margin-bottom:6px; color:#e2e8f0;"),
                        Input(type="password", name="password", placeholder="Senha", style="width:100%; padding:10px 12px; border-radius:8px; border:1px solid #475569; margin-bottom:16px;"),
                        Button("Criar usuário", type="submit", style="width:100%; padding:10px 12px; border:none; border-radius:8px; background:#34d399; color:#052e16; font-weight:bold; cursor:pointer; margin-bottom:10px;"),
                        action="/admin/create",
                        method="get",
                        style="display:flex; flex-direction:column;"
                    ),
                    Table(
                        Thead(Tr(Th("ID"), Th("Usuário"), Th("Ação"))),
                        Tbody(*rows) if rows else Tbody(Tr(Td("Nenhum usuário encontrado", colspan="3")))
                    , style="width:100%; border-collapse:collapse; margin-top:20px; background:#fff; color:#111827;"),
                    A("Voltar ao login", href="/", style="display:block; margin-top:18px; color:#7dd3fc; text-align:center; text-decoration:none; font-weight:bold;"),
                    style="max-width:min(640px, calc(100% - 24px)); margin:40px auto; padding:clamp(20px, 4vw, 34px); border-radius:28px; background:linear-gradient(145deg, rgba(2, 6, 23, 0.98), rgba(37, 99, 235, 0.9)); box-shadow:0 25px 70px rgba(2, 6, 23, 0.6); border:2px solid rgba(125, 211, 252, 0.4); box-sizing:border-box;"
                ),
                style="min-height:70vh; background:radial-gradient(circle at top, #1d4ed8 0%, #020617 70%); padding:20px 0;"
            )
        ),
        Footer(
            P("© 2026 Projeto Espaço Viagem - Desenvolvido para estudos de programação e astronomia.", style="text-align:center; color:#cbd5e1; padding:20px 0;")
        )
    )


def layout_cadastro(error_message: str = None, success_message: str = None):
    feedback = None
    if error_message:
        feedback = P(error_message, style="color:#fda4af; margin-bottom:12px;")
    elif success_message:
        feedback = P(success_message, style="color:#86efac; margin-bottom:12px;")

    return (
        Header(
            H1("📝 Criar conta", style="text-align:center; margin:0; color:#f8fafc;"),
            style="background:linear-gradient(135deg, #020617, #2563eb); padding:24px 20px;"
        ),
        Main(
            Section(
                Div(
                    H2("Cadastre um novo usuário", style="margin:0 0 8px; color:#f8fafc;"),
                    P("Preencha os campos abaixo para criar sua conta.", style="margin:0 0 16px; color:#cbd5e1;"),
                    feedback,
                    Form(
                        Label("Usuário", style="display:block; margin-bottom:6px; color:#e2e8f0;"),
                        Input(type="text", name="username", placeholder="Escolha um usuário", style="width:100%; padding:10px 12px; border-radius:8px; border:1px solid #475569; margin-bottom:12px;"),
                        Label("Senha", style="display:block; margin-bottom:6px; color:#e2e8f0;"),
                        Input(type="password", name="password", placeholder="Escolha uma senha", style="width:100%; padding:10px 12px; border-radius:8px; border:1px solid #475569; margin-bottom:16px;"),
                        Button("Criar conta", type="submit", style="width:100%; padding:10px 12px; border:none; border-radius:8px; background:#34d399; color:#052e16; font-weight:bold; cursor:pointer; margin-bottom:10px;"),
                        action="/cadastrar",
                        method="get",
                        style="display:flex; flex-direction:column;"
                    ),
                    A("Voltar para entrar", href="/", style="display:block; margin-top:8px; color:#7dd3fc; text-align:center; text-decoration:none; font-weight:bold;"),
                    style="max-width:440px; margin:60px auto; padding:34px; border-radius:28px; background:linear-gradient(145deg, rgba(2, 6, 23, 0.98), rgba(37, 99, 235, 0.9)); box-shadow:0 25px 70px rgba(2, 6, 23, 0.6); border:2px solid rgba(125, 211, 252, 0.4);"
                ),
                style="min-height:70vh; background:radial-gradient(circle at top, #1d4ed8 0%, #020617 70%); padding:20px 0;"
            )
        ),
        Footer(
            P("© 2026 Projeto Espaço Viagem - Desenvolvido para estudos de programação e astronomia.", style="text-align:center; color:#cbd5e1; padding:20px 0;")
        )
    )


def layout_tabela_usuarios(usuarios):
    rows = [Tr(Td(user["id"]), Td(user["username"])) for user in usuarios]
    return (
        Header(
            H1("👤 Usuários cadastrados", style="text-align:center; margin:0; color:#f8fafc;"),
            style="background:linear-gradient(135deg, #020617, #2563eb); padding:24px 20px;"
        ),
        Main(
            Section(
                Table(
                    Thead(
                        Tr(
                            Th("ID"),
                            Th("Usuário")
                        )
                    ),
                    Tbody(*rows) if rows else Tbody(Tr(Td("Nenhum usuário encontrado", colspan="2")))
                , style="width:100%; border-collapse:collapse; background:#fff; color:#111827;"),
                style="max-width:min(700px, calc(100% - 24px)); margin:40px auto; padding:clamp(16px, 3vw, 20px); border-radius:16px; background:rgba(15, 23, 42, 0.9); box-shadow:0 16px 40px rgba(0,0,0,0.25); box-sizing:border-box;"
            ),
            P(A("Voltar ao login", href="/", style="display:block; text-align:center; color:#7dd3fc; margin-top:20px;"))
        ),
        Footer(
            P("© 2026 Projeto Espaço Viagem - Desenvolvido para estudos de programação e astronomia.", style="text-align:center; color:#cbd5e1; padding:20px 0;")
        )
    )


def layout_pagina_inicial():
    # Retorna as partes principais que compõem o corpo do site
    return (
        # 1. CABEÇALHO E NAVEGAÇÃO
        Header(
            H1("🚀 Espaço Viagem 🚀", style="margin:0; color:#f8fafc;"),
            Nav(
                Ul(
                    Li(A("Início", href="/", style="color:#f8fafc; text-decoration:none;")),
                    Li(A("Planetas (Em breve)", href="#", style="color:#f8fafc; text-decoration:none;")),
                    Li(A("Asteroides (Em breve)", href="#", style="color:#f8fafc; text-decoration:none;")),
                    Li(A("Sobre a Equipe", href="#", style="color:#f8fafc; text-decoration:none;"))
                , style="display:flex; gap:16px; list-style:none; padding:0; margin:12px 0 0; flex-wrap:wrap;"),
                style="margin-top:10px;"
            ),
            style="background:linear-gradient(135deg, #020617, #1d4ed8); padding:24px 16px;"
        ),

        # 2. CONTEÚDO PRINCIPAL
        Main(
            Section(
                Div(
                    H2("Bem-vindo ao Cosmos!", style="margin:0 0 10px; color:#f8fafc;"),
                    P("Este é o ambiente inicial do projeto Espaço Viagem, desenvolvido por Ramon, Samira, Emmanuel e Pyerre.", style="color:#cbd5e1; line-height:1.6;"),
                    P("Aqui vamos explorar imagens da NASA e dados da Wikipedia sobre o nosso sistema solar.", style="color:#cbd5e1; line-height:1.6;"),
                    P("Sua jornada espacial começou com sucesso.", style="margin-top:16px; font-weight:bold; color:#38bdf8;")
                , style="max-width:min(760px, calc(100% - 24px)); margin:0 auto; padding:clamp(20px, 4vw, 32px); background:rgba(15, 23, 42, 0.8); border-radius:20px; box-shadow:0 16px 40px rgba(0,0,0,0.25); box-sizing:border-box;"),
                style="padding:40px 16px; background:radial-gradient(circle at top, #1e3a8a 0%, #020617 70%);"
            ),

            # Seção 2: Espaço reservado...
            Section(
                H2("Imagem Astronômica do Dia", style="color:#f8fafc;"),
                P("Em breve, este espaço receberá os dados integrados da API da NASA.", style="color:#cbd5e1;")
            , style="padding:20px 16px; max-width:min(760px, calc(100% - 24px)); margin:20px auto 0; box-sizing:border-box;")
        ),

        # 3. RODAPÉ
        Footer(
            P("© 2026 Projeto Espaço Viagem - Desenvolvido para estudos de programação e astronomia.", style="text-align:center; color:#cbd5e1; padding:20px 0;")
        )
    )


