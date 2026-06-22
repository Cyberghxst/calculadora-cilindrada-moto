# 🏍️ Calculadora de Cilindrada para Motos

Una aplicación de escritorio moderna y fácil de usar, desarrollada en **Python** con **CustomTkinter**, que calcula la cilindrada (volumen total de los cilindros) de un motor de moto a partir del diámetro del pistón (bore), la carrera (stroke) y el número de cilindros.

![Versión Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2.0%2B-green)
![Licencia](https://img.shields.io/badge/Licencia-MIT-yellow)

---

## ✨ Características

- ✅ **Interfaz moderna** con tema oscuro y colores atractivos.
- ✅ **Soporte para cm y mm** en cada medida de forma independiente.
- ✅ **Conversión automática** a centímetros para aplicar la fórmula correcta.
- ✅ **Validación de datos** en tiempo real: detecta valores negativos, cero o entradas no numéricas.
- ✅ **Resultados claros** en **cm³ (cc)** y **Litros**.
- ✅ **Footer informativo** que muestra la fórmula y los valores convertidos.
- ✅ **Totalmente portable**: no requiere dependencias externas más allá de Python y CustomTkinter.

---

## 🧮 Fórmula utilizada

La cilindrada se calcula con la siguiente fórmula:

```
Cilindrada (cm³) = (π / 4) × Bore² × Stroke × Número de cilindros
```

Donde:
- **Bore** = Diámetro del pistón (en cm)
- **Stroke** = Carrera del pistón (en cm)
- **N** = Número de cilindros del motor

---

## 📦 Requisitos previos

- **Python 3.8 o superior** instalado en tu sistema.
- La librería **CustomTkinter** (instalable vía pip).

---

## 🔧 Instalación y ejecución

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/Cyberghxst/calculadora-cilindrada-moto.git
cd calculadora-cilindrada-moto
```

### 2. Instalar dependencias

```bash
pip install customtkinter
```

### 3. Ejecutar la aplicación

```bash
python calculadora.py
```

*(Asegúrate de que el archivo Python tenga el nombre correcto, por ejemplo `main.py` o `calculadora.py`)*

---

## 🚀 Cómo usar la aplicación

1. Introduce el **diámetro del pistón (Bore)** en el campo correspondiente.
2. Selecciona la unidad (**cm** o **mm**) en el desplegable.
3. Introduce la **carrera del pistón (Stroke)** y selecciona su unidad.
4. Introduce el **número de cilindros** del motor.
5. Pulsa el botón **"Calcular Cilindrada"**.
6. Visualiza el resultado en **cm³ (cc)** y en **Litros**.

### Ejemplo práctico

| Parámetro      | Valor  | Unidad |
|----------------|--------|--------|
| Bore           | 6.7    | cm     |
| Stroke         | 6.6    | cm     |
| Cilindros      | 2      | -      |

**Resultado esperado:** `465.13 cm³ (0.465 Litros)`

---

## 🛠️ Tecnologías utilizadas

- **Python 3** – Lenguaje de programación principal.
- **CustomTkinter** – Framework moderno para interfaces gráficas basado en Tkinter.
- **Math** – Librería estándar para operaciones matemáticas (π).

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama: `git checkout -b feature/nueva-funcionalidad`
3. Realiza tus cambios y haz commit: `git commit -m 'Añadir nueva funcionalidad'`
4. Sube los cambios: `git push origin feature/nueva-funcionalidad`
5. Abre un **Pull Request**.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## ✍️ Autor

Desarrollado por **Cyberghxst** – [Cyberghxst](https://github.com/Cyberghxst)

Si te ha gustado este proyecto, ¡no olvides darle una ⭐ en GitHub!

---

## 📬 Contacto

Para cualquier duda, sugerencia o reporte de error, puedes abrir un **Issue** en el repositorio o contactarme directamente a través de mi perfil de GitHub.

---

**¡Disfruta calculando la cilindrada de tu moto! 🏍️💨**
