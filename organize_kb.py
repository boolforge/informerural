import os
import re
import hashlib
import json
from collections import defaultdict
import shutil

# This script performs the initial knowledge base organization.
# It reads all files, processes them in memory, and then writes the final
# structure to a new 'base_de_conocimiento' directory.

# --- Configuration: Define the final structure and name mappings ---

FILE_MAPPINGS = {
    # Metodología
    "00_philosophical_directive": "metodologia/00_directiva_filosofica.md",
    "00_role_and_philosophical_directive": "metodologia/01_rol_y_directiva.md",
    "0_1_personal_needs_passport": "metodologia/02_pasaporte_de_necesidades.md",
    "0_lifestyle_values": "metodologia/03_valores_estilo_de_vida.md",
    "0_phase_analytical_prism": "metodologia/04_prisma_analitico.md",
    "0_scope_exclusions_preferences": "metodologia/05_alcance_y_exclusiones.md",
    "1_methodological_summary": "metodologia/06_resumen_metodologico.md",
    "1_required_final_products": "metodologia/07_productos_finales_requeridos.md",
    "2_data_quality_rule": "metodologia/08_regla_calidad_de_datos.md",
    "2_data_sources": "metodologia/09_fuentes_de_datos.md",
    "3_indicators_and_operational_definition": "metodologia/10_indicadores_y_definicion.md",
    "4_hard_discard_criteria": "metodologia/11_criterios_de_descarte.md",
    "5_geographic_coverage_subzones": "metodologia/12_cobertura_geografica.md",
    "6_output_schema": "metodologia/13_esquema_de_salida.md",
    "7_methodological_transparency": "metodologia/14_transparencia_metodologica.md",
    "7_quantitative_methodology": "metodologia/15_metodologia_cuantitativa.md",
    "8_respiratory_specific_rules": "metodologia/16_reglas_respiratorias.md",
    "11_format_and_style": "metodologia/17_formato_y_estilo.md",
    "11_inventory_of_sources": "metodologia/18_inventario_de_fuentes.md",
    "15_methodological_nuances": "metodologia/19_matices_metodologicos.md",
    "protocolo_investigacion": "metodologia/20_protocolo_investigacion.md",
    "rural_urban_classification_methodology": "metodologia/21_clasificacion_rural_urbana_metodologia.md",
    "progress_template_details": "metodologia/22_plantilla_de_progreso.md",

    # Investigación - Temas
    "investigacion_ecosistema_natural": "investigacion/temas/01_ecosistema_natural.md",
    "investigacion_macro_contextual": "investigacion/temas/02_macro_contextual.md",
    "investigacion_preliminar": "investigacion/temas/03_preliminar.md",
    "paramanus_notes": "investigacion/temas/04_notas_paramanus.md",
    "paramanus_extracted_info": "investigacion/temas/05_info_extraida_paramanus.md",
    "rural_localities_uk": "investigacion/temas/06_localidades_rurales_uk.md",
    "rural_urban_classification_uk": "investigacion/temas/07_clasificacion_rural_urbana_uk.md",
    "2_key_clinical_observations": "investigacion/temas/08_observaciones_clinicas.md",
    "5_numeric_pollen_block": "investigacion/temas/09_bloque_numerico_polen.md",
    "6_quick_clinical_summary": "investigacion/temas/10_resumen_clinico_rapido.md",

    # Investigación - Textos Crudos (a revisar)
    "arepasar": "investigacion/textos_crudos/arepasar.txt",
    "paramanus": "investigacion/textos_crudos/paramanus.txt",
    "pasted_content": "investigacion/textos_crudos/contenido_pegado.txt",
    "todo": "investigacion/textos_crudos/todo.txt",
    "script_output": "investigacion/textos_crudos/script_output.txt",

    # Investigación - Países
    "denmark_housing_costs": "investigacion/paises/dinamarca_costes_vivienda.md",
    "finland_housing_costs": "investigacion/paises/finlandia_costes_vivienda.md",
    "france_housing_costs": "investigacion/paises/francia_costes_vivienda.md",
    "germany_housing_costs": "investigacion/paises/alemania_costes_vivienda.md",
    "ireland_housing_costs": "investigacion/paises/irlanda_costes_vivienda.md",
    "irlanda_costes_vivienda": "investigacion/paises/irlanda_costes_vivienda.md", # Consolida aquí
    "netherlands_housing_costs": "investigacion/paises/paises_bajos_costes_vivienda.md",
    "portugal_housing_costs": "investigacion/paises/portugal_costes_vivienda.md",
    "spain_housing_costs": "investigacion/paises/espana_costes_vivienda.md",
    "sweden_housing_costs": "investigacion/paises/suecia_costes_vivienda.md",

    # Informes
    "documento_final": "informes/01_documento_final.md",
    "introduction_title": "informes/02_introduccion.md",
    "section_titles": "informes/03_titulos_de_seccion.md",
    "report_target_audience_note": "informes/04_nota_audiencia_objetivo.md",
    "9_final_selection_narrative": "informes/05_narrativa_seleccion_final.md",
    "8_immediate_recommendation": "informes/06_recomendacion_inmediata.md",
    "3_practical_recommendation": "informes/07_recomendacion_practica.md",
    "4_next_steps_prompt": "informes/08_proximos_pasos_prompt_1.md",
    "9_next_steps_prompt": "informes/09_proximos_pasos_prompt_2.md",
    "14_practical_conclusion_gadm": "informes/10_conclusion_practica_gadm.md",
    "10_minimum_visualizations": "informes/11_visualizaciones_minimas.md",
    "12_progress_template": "informes/12_plantilla_progreso.md",

    # Configuración
    "_": "configuracion/cdsapirc",
}

# --- Helper Functions ---

def get_basename(filename):
    """Gets the basename of a file by removing numeric suffixes and handling special cases."""
    if "Notas_de_Análisis_Detallado_de_paramanus" in filename:
        return "paramanus_notes"
    if "Irlanda_(Detalle_Adicional_de_Costes_de_Vivienda" in filename:
        return "irlanda_costes_vivienda"

    name_part, _ = os.path.splitext(filename)
    if name_part.endswith('.cs'):
        name_part = name_part[:-3]

    base = re.sub(r'(_\d+)+$', '', name_part)
    return base

def get_file_hash(content):
    """Computes the SHA256 hash of file content."""
    return hashlib.sha256(content.encode('utf-8', 'ignore')).hexdigest()

# --- Main Logic ---

def main():
    print("Starting knowledge base organization...")
    base_dir = "base_de_conocimiento"

    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
        print(f"Removed existing directory: {base_dir}")

    # 1. Read all files into memory
    all_files = [f for f in os.listdir('.') if os.path.isfile(f) and f != "organize_kb.py"]
    file_contents = {}
    for filename in all_files:
        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                file_contents[filename] = f.read()
        except Exception:
            file_contents[filename] = None

    # 2. Group files by basename
    grouped_by_basename = defaultdict(list)
    for filename in all_files:
        basename = get_basename(filename)
        grouped_by_basename[basename].append(filename)

    # 3. Consolidate content in memory
    final_content_map = {}

    for basename, file_list in grouped_by_basename.items():
        hashes = defaultdict(list)
        for filename in file_list:
            content = file_contents.get(filename)
            if content is not None:
                hashes[get_file_hash(content)].append(filename)

        merged_content = ""
        separator = f"\\n\\n--- Contenido de archivo original: {', '.join(file_list)} ---\\n\\n"

        sorted_hashes = sorted(hashes.items(), key=lambda item: item[1][0])

        for i, (h, files) in enumerate(sorted_hashes):
            content_to_add = file_contents[files[0]]
            if i > 0:
                merged_content += separator
            merged_content += content_to_add

        final_path = FILE_MAPPINGS.get(basename)
        if final_path:
            final_content_map[os.path.join(base_dir, final_path)] = merged_content
        else:
            ext = os.path.splitext(file_list[0])[1].lower()
            if ext == '.py':
                final_path = os.path.join(base_dir, "scripts", os.path.basename(file_list[0]))
            elif ext in ['.csv', '.json']:
                 final_path = os.path.join(base_dir, "datos/crudos", os.path.basename(file_list[0]))
            elif ext in ['.png', '.jpg', '.jpeg', '.gif']:
                 final_path = os.path.join(base_dir, "imagenes", os.path.basename(file_list[0]))
                 final_content_map[final_path] = None
            else:
                 final_path = os.path.join(base_dir, "investigacion/otros", os.path.basename(file_list[0]))

            if final_path in final_content_map and final_content_map[final_path] is not None:
                 final_content_map[final_path] += separator + merged_content
            else:
                 final_content_map[final_path] = merged_content

    # 4. Write the new structure to disk
    print("Writing the new knowledge base structure...")
    log = []
    for final_path, content in final_content_map.items():
        try:
            dir_name = os.path.dirname(final_path)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            if content is not None:
                with open(final_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                log.append(f"CREATED: {final_path}")
            else:
                original_filename = os.path.basename(final_path)
                shutil.copyfile(original_filename, final_path)
                log.append(f"COPIED: {final_path}")

        except Exception as e:
            log.append(f"ERROR creating {final_path}: {e}")

    # 5. Write log file
    with open("kb_organization_log.txt", 'w') as f:
        f.write("\\n".join(log))

    print("Organization complete. See kb_organization_log.txt for details.")

if __name__ == "__main__":
    main()
