import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo global
sns.set_theme(style="whitegrid")

# --- 1. plot_gradient_bar (Versión Seaborn) ---
def plot_gradient_bar(labels, values, gradients, title, bar_width=0.6, height=500):
    """
    Crea un gráfico de barras usando Seaborn.
    Convierte los gradientes (tuplas de colores) en colores sólidos.
    """
    # Convertimos altura de px a pulgadas (aprox) para matplotlib
    fig_height = height / 100
    fig, ax = plt.subplots(figsize=(10, fig_height))
    
    # Procesamos los colores: si vienen tuplas (gradientes), cogemos el primer color
    # Si viene una lista simple, la usamos tal cual.
    if gradients and isinstance(gradients[0], (list, tuple)):
        palette = [g[0] for g in gradients]
    else:
        palette = gradients

    # Crear el gráfico
    sns.barplot(x=labels, y=values, palette=palette, ax=ax, edgecolor="black", linewidth=0.5)
    
    # Añadir números encima de las barras
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f', padding=3, fontsize=10)

    # Personalización
    ax.set_title(title, fontsize=16, pad=20)
    ax.set_ylabel("Count")
    ax.set_xlabel("")
    
    # Rotar etiquetas si hay muchas
    if len(labels) > 5:
        plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    # Devolvemos el objeto 'fig' para que funcione con save_and_display
    return fig

# --- 2. save_and_display ---
def save_and_display(fig, filename):
    """
    Guarda la figura como PNG y la muestra.
    """
    try:
        # Guardamos en PNG porque matplotlib no suele guardar en HTML interactivo
        # fig.savefig(f"../plots/{filename}.png", dpi=300, bbox_inches='tight')
        print(f"Imagen guardada como: {filename}.png")
    except Exception as e:
        print(f"No se pudo guardar la imagen: {e}")
    
    # En matplotlib, 'show' se suele llamar al final. 
    # Si estamos en Jupyter, fig ya se mostrará al retornarla o con plt.show()
    plt.show()

# --- 3. plot_stacked_categorical_gradient ---
def plot_stacked_categorical_gradient(df, col, title, bar_width=0.55, height=500):
    """
    Gráfico de barras apiladas (Stacked Bar) con Matplotlib/Pandas.
    Muestra Default vs No Default.
    """
    # Preparar datos
    cross_tab = pd.crosstab(df[col], df['loan_status_binary'])
    # Ordenar por volumen total
    cross_tab['total'] = cross_tab[0] + cross_tab[1]
    cross_tab = cross_tab.sort_values('total', ascending=False).drop('total', axis=1)
    
    # Definir colores (Rojo para Default/0, Azul para No Default/1)
    # Ajusta el orden según tus columnas [0, 1]
    colors = ['#ff6b6b', '#4d7cfe'] 
    
    fig_height = height / 100
    fig, ax = plt.subplots(figsize=(10, fig_height))
    
    # Plot apilado directo desde pandas (usa matplotlib por debajo)
    cross_tab.plot(kind='bar', stacked=True, color=colors, ax=ax, width=bar_width, edgecolor='none')
    
    ax.set_title(title, fontsize=16)
    ax.set_ylabel("Number of Applicants")
    ax.set_xlabel(col)
    ax.legend(title='Loan Status', labels=['Default (0)', 'No Default (1)'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return fig

# --- 4. plot_woe_distribution_plotly (Implementación en Seaborn) ---
def plot_woe_distribution_plotly(woe_df, iv_df=None):
    """
    Mantiene el nombre '_plotly' para compatibilidad, pero usa Matplotlib.
    Eje izquierdo: WoE (Línea). Eje derecho: Event Rate (Barras).
    """
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Eje derecho: Tasa de eventos (Barras)
    ax2 = ax1.twinx()
    if 'event_rate' in woe_df.columns:
        sns.barplot(data=woe_df, x='sub_name', y='event_rate', ax=ax2, color='gray', alpha=0.3)
        ax2.set_ylabel('Event Rate')
        ax2.grid(False) # Quitar rejilla del segundo eje para limpieza

    # Eje izquierdo: WoE (Línea con puntos)
    sns.lineplot(data=woe_df, x='sub_name', y='woe', marker='o', color='black', linewidth=2, ax=ax1)
    ax1.set_ylabel('WoE (Weight of Evidence)', color='black')
    ax1.tick_params(axis='y', labelcolor='black')
    
    # Título dinámico con IV
    title = "WoE Distribution"
    if iv_df is not None and not iv_df.empty:
        col_name = woe_df['name'].iloc[0] if 'name' in woe_df.columns else woe_df.columns[0]
        try:
            iv_val = iv_df[iv_df['Column'] == col_name]['IV'].values[0]
            title += f" (IV: {iv_val:.4f})"
        except:
            pass

    plt.title(title, fontsize=16)
    
    # Ajuste de etiquetas eje X
    ax1.set_xlabel("Bin / Category")
    # Rotar etiquetas si son muchas
    if len(woe_df) > 5:
        for tick in ax1.get_xticklabels():
            tick.set_rotation(45)
            
    plt.tight_layout()
    return fig

# --- 5. plot_gradient_bar_grouped ---
def plot_gradient_bar_grouped(df, col, target, title):
    """
    Gráfico de barras agrupadas con Seaborn.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.countplot(data=df, x=col, hue=target, palette=['#ff6b6b', '#4d7cfe'], ax=ax)
    
    ax.set_title(title, fontsize=16)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return fig

# --- 6. plot_pie ---
def plot_pie(labels, values, title, height=500):
    """
    Crea un gráfico de pastel (quesito) usando Matplotlib pero con estilo Seaborn.
    Muestra porcentajes y etiquetas.
    """
    # Configuración de tamaño
    fig_height = height / 100
    fig, ax = plt.subplots(figsize=(8, fig_height))
    
    # Definir colores usando una paleta de Seaborn (ej. 'pastel' o 'Set2')
    # Ajustamos la cantidad de colores al número de etiquetas
    colors = sns.color_palette('pastel')[0:len(labels)]
    
    # Crear el gráfico
    # autopct='%1.1f%%': Muestra el porcentaje con 1 decimal
    # startangle=90: Empieza a rotar desde arriba (más estético)
    # pctdistance=0.85: Pone el % un poco más lejos del centro
    wedges, texts, autotexts = ax.pie(
        values, 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%', 
        startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1}, # Bordes blancos estilo moderno
        textprops={'fontsize': 11}
    )
    
    # Personalización de los textos de porcentaje (opcional, para que se vean mejor)
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_weight('bold')

    ax.set_title(title, fontsize=16, pad=20)
    plt.tight_layout()
    
    return fig