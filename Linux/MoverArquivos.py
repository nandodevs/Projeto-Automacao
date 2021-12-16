import os
import argparse

parser = argparse.ArgumentParser(
    description="Limpar o diretório e mover os arquivos de acordo com o formato."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="O diretório será totalmente limpo",
)

args = parser.parse_args()
path = args.path

print(f"Limpando o diretório {path} ...")
