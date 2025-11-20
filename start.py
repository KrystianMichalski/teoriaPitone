from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'SOLUZIONE DOCENTE: Mini-Gestionale Libri', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, 'Esercitazione 50 min - Classi 3^/4^ - Logica Python', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Pagina {self.page_no()}', 0, 0, 'C')

def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # --- SEZIONE 1: ANALISI DEI TODO ---
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Parte 1: Analisi dei TODO", 0, 1)
    pdf.set_font("Arial", '', 12)
    
    text_intro = (
        "Di seguito sono riportate le soluzioni puntuali per le tre parti mancanti "
        "dell'esercizio, con note su cosa verificare nel codice degli studenti."
    )
    pdf.multi_cell(0, 7, text_intro)
    pdf.ln(5)

    # TODO 1
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "TODO 1: Creazione del Dizionario", 0, 1)
    pdf.set_font("Courier", '', 11)
    pdf.set_fill_color(240, 240, 240)
    code_todo1 = """
    nuovo_libro = {
        "titolo": titolo,
        "autore": autore,
        "isbn": isbn
    }
    """
    pdf.multi_cell(0, 6, code_todo1, 1, 'L', True)
    pdf.set_font("Arial", 'I', 10)
    pdf.multi_cell(0, 6, "Nota: Verificare che usino le virgolette per le chiavi (es. \"titolo\") e i due punti corretti.")
    pdf.ln(5)

    # TODO 2
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "TODO 2: Ciclo di Ricerca", 0, 1)
    pdf.set_font("Courier", '', 11)
    code_todo2 = """
    for libro in archivio_libri:
        if libro["autore"] == autore_da_cercare:
            print(f"Trovato: {libro['titolo']}")
            trovato = True
    """
    pdf.multi_cell(0, 6, code_todo2, 1, 'L', True)
    pdf.set_font("Arial", 'I', 10)
    pdf.multi_cell(0, 6, "Nota: Fondamentale l'indentazione sotto l'IF. Alcuni studenti potrebbero dimenticare il doppio uguale (==) per il confronto.")
    pdf.ln(5)

    # TODO 3
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "TODO 3: Chiamate nel Main", 0, 1)
    pdf.set_font("Courier", '', 11)
    code_todo3 = """
    aggiungi_libro("1984", "Orwell", "978-123")
    cerca_libro_per_autore("Orwell")
    mostra_tutti()
    """
    pdf.multi_cell(0, 6, code_todo3, 1, 'L', True)
    pdf.ln(10)

    # --- SEZIONE 2: CODICE COMPLETO ---
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Parte 2: Codice Python Completo", 0, 1)
    pdf.set_font("Arial", '', 10)
    pdf.multi_cell(0, 6, "Copia e incolla questo codice per mostrare il funzionamento corretto alla LIM.")
    pdf.ln(5)

    pdf.set_font("Courier", '', 9)
    full_code = """
# --- STRUTTURA DATI ---
archivio_libri = []

# --- FUNZIONI ---

def aggiungi_libro(titolo, autore, isbn):
    # Creazione del dizionario (TODO 1 RISOLTO)
    nuovo_libro = {
        "titolo": titolo,
        "autore": autore,
        "isbn": isbn
    }
    
    archivio_libri.append(nuovo_libro)
    print(f"Libro '{titolo}' aggiunto con successo!")

def cerca_libro_per_autore(autore_da_cercare):
    print(f"--- Ricerca libri di: {autore_da_cercare} ---")
    trovato = False
    
    # Ciclo e confronto (TODO 2 RISOLTO)
    for libro in archivio_libri:
        if libro["autore"] == autore_da_cercare:
            print(f"- Trovato: {libro['titolo']} (ISBN: {libro['isbn']})")
            trovato = True
            
    if not trovato:
        print("Nessun libro trovato per questo autore.")

def mostra_tutti():
    print("--- TUTTI I LIBRI ---")
    for libro in archivio_libri:
        print(f"- {libro['titolo']} (Autore: {libro['autore']})")

# --- MAIN ---

# Dati di prova iniziali
archivio_libri.append({"titolo": "Harry Potter", "autore": "Rowling", "isbn": "111"})
archivio_libri.append({"titolo": "Il Signore degli Anelli", "autore": "Tolkien", "isbn": "222"})

# Test delle funzioni (TODO 3 RISOLTO)
print("--- INIZIO TEST ---")
aggiungi_libro("Il Piccolo Principe", "Saint-Exupery", "333")

# Test ricerca positiva
cerca_libro_per_autore("Tolkien")

# Test ricerca negativa
cerca_libro_per_autore("Manzoni")

# Mostra stato finale
mostra_tutti()
    """
    pdf.multi_cell(0, 5, full_code, 1, 'L', True)

    # Output file
    pdf.output("Soluzione_Docente_Libri.pdf")
    print("PDF creato con successo: 'Soluzione_Docente_Libri.pdf'")

if __name__ == "__main__":
    try:
        create_pdf()
    except Exception as e:
        print(f"Errore: {e}")
        print("Assicurati di aver installato fpdf: pip install fpdf")
