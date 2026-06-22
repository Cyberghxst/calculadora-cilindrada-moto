import customtkinter as ctk
import math

# Configurar tema y apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CalculadoraCilindrada(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Calculadora de Cilindrada - Moto")
        self.geometry("500x600")
        self.resizable(False, False)
        
        # Título principal
        self.titulo = ctk.CTkLabel(
            self, 
            text="🏍️ Calculadora de Cilindrada", 
            font=("Arial", 24, "bold")
        )
        self.titulo.pack(pady=20)
        
        # Frame para los inputs
        self.frame_inputs = ctk.CTkFrame(self)
        self.frame_inputs.pack(pady=10, padx=20, fill="both")
        
        # Campo: Diámetro (bore)
        self.label_bore = ctk.CTkLabel(
            self.frame_inputs, 
            text="Diámetro del pistón (Bore):", 
            font=("Arial", 14)
        )
        self.label_bore.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_bore = ctk.CTkEntry(
            self.frame_inputs, 
            placeholder_text="Ej: 6.7", 
            width=120
        )
        self.entry_bore.grid(row=0, column=1, padx=10, pady=10)
        
        self.unidad_bore = ctk.CTkComboBox(
            self.frame_inputs,
            values=["cm", "mm"],
            width=80
        )
        self.unidad_bore.grid(row=0, column=2, padx=10, pady=10)
        self.unidad_bore.set("cm")
        
        # Campo: Carrera (stroke)
        self.label_stroke = ctk.CTkLabel(
            self.frame_inputs, 
            text="Carrera del pistón (Stroke):", 
            font=("Arial", 14)
        )
        self.label_stroke.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_stroke = ctk.CTkEntry(
            self.frame_inputs, 
            placeholder_text="Ej: 6.6", 
            width=120
        )
        self.entry_stroke.grid(row=1, column=1, padx=10, pady=10)
        
        self.unidad_stroke = ctk.CTkComboBox(
            self.frame_inputs,
            values=["cm", "mm"],
            width=80
        )
        self.unidad_stroke.grid(row=1, column=2, padx=10, pady=10)
        self.unidad_stroke.set("cm")
        
        # Campo: Número de cilindros
        self.label_cilindros = ctk.CTkLabel(
            self.frame_inputs, 
            text="Número de cilindros:", 
            font=("Arial", 14)
        )
        self.label_cilindros.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_cilindros = ctk.CTkEntry(
            self.frame_inputs, 
            placeholder_text="Ej: 2", 
            width=120
        )
        self.entry_cilindros.grid(row=2, column=1, padx=10, pady=10)
        
        # Botón calcular
        self.btn_calcular = ctk.CTkButton(
            self,
            text="🔧 Calcular Cilindrada",
            command=self.calcular,
            font=("Arial", 16, "bold"),
            height=45
        )
        self.btn_calcular.pack(pady=20)
        
        # Frame para resultados
        self.frame_resultado = ctk.CTkFrame(self)
        self.frame_resultado.pack(pady=10, padx=20, fill="both")
        
        self.label_resultado = ctk.CTkLabel(
            self.frame_resultado,
            text="Resultado:",
            font=("Arial", 16, "bold")
        )
        self.label_resultado.pack(pady=5)
        
        self.label_cc = ctk.CTkLabel(
            self.frame_resultado,
            text="--- cm³ (cc)",
            font=("Arial", 20, "bold"),
            text_color="#00cc66"
        )
        self.label_cc.pack(pady=5)
        
        self.label_litros = ctk.CTkLabel(
            self.frame_resultado,
            text="--- Litros",
            font=("Arial", 14),
            text_color="#66ccff"
        )
        self.label_litros.pack(pady=5)
        
        # Label para errores
        self.label_error = ctk.CTkLabel(
            self,
            text="",
            font=("Arial", 12),
            text_color="#ff6666"
        )
        self.label_error.pack(pady=5)
        
        # Footer con información
        self.footer = ctk.CTkLabel(
            self,
            text="Fórmula: (π/4) × Bore² × Stroke × N° Cilindros",
            font=("Arial", 12),
            text_color="gray"
        )
        self.footer.pack(pady=10)
    
    def convertir_a_cm(self, valor, unidad):
        """Convierte mm a cm si es necesario"""
        if unidad == "mm":
            return valor / 10.0
        return valor
    
    def calcular(self):
        # Limpiar mensaje de error
        self.label_error.configure(text="")
        
        try:
            # Obtener valores
            bore = float(self.entry_bore.get().replace(",", "."))
            stroke = float(self.entry_stroke.get().replace(",", "."))
            cilindros = int(self.entry_cilindros.get())
            
            # Validar números positivos
            if bore <= 0 or stroke <= 0 or cilindros <= 0:
                raise ValueError("Todos los valores deben ser positivos")
            
            # Convertir a cm si están en mm
            bore_cm = self.convertir_a_cm(bore, self.unidad_bore.get())
            stroke_cm = self.convertir_a_cm(stroke, self.unidad_stroke.get())
            
            # Calcular cilindrada
            # Fórmula: (π/4) × D² × C × N
            cilindrada = (math.pi / 4) * (bore_cm ** 2) * stroke_cm * cilindros
            
            # Mostrar resultados
            self.label_cc.configure(text=f"{cilindrada:.2f} cm³ (cc)")
            self.label_litros.configure(text=f"{cilindrada / 1000:.3f} Litros")
            
            # Mostrar datos usados en la conversión (info adicional)
            unidad_mostrada = "mm" if self.unidad_bore.get() == "mm" else "cm"
            self.footer.configure(
                text=f"Bore: {bore:.2f} {unidad_mostrada} → {bore_cm:.3f} cm | "
                     f"Stroke: {stroke:.2f} {unidad_mostrada} → {stroke_cm:.3f} cm | "
                     f"Cilindros: {cilindros}"
            )
            
        except ValueError as e:
            self.label_error.configure(text=f"❌ Error: {str(e)}")
            self.label_cc.configure(text="--- cm³ (cc)")
            self.label_litros.configure(text="--- Litros")
        except Exception as e:
            self.label_error.configure(text=f"❌ Error inesperado: {str(e)}")
