from googleapiclient.discovery import build


MY_API_KEY = "AIzaSyAD5_CMDH_RhNYP6qDmwL2uZuVNIs5XrQ4" 
MY_CX_ID = "0609deef8cd0a4abb"

def internetde_fayl_axtar(movzu, fayl_tipi):
    try:
        # Google Custom Search API servisini qururuq
        service = build("customsearch", "v1", developerKey=MY_API_KEY)
        
        # Axtarış sorğusunu hazırlayırıq
        tam_sorgu = f"{movzu} filetype:{fayl_tipi}"
        
        # Google-dan nəticələri istəyirik
        netice = service.cse().list(
            q=tam_sorgu, 
            cx=MY_CX_ID,
            num=10  # İlk 10 nəticəni gətirir
        ).execute()
        
        if 'items' in netice:
            print(f"\n✅ '{movzu}' mövzusunda {fayl_tipi} faylları tapıldı:\n")
            print("-" * 50)
            for i, item in enumerate(netice['items'], 1):
                basliq = item.get('title')
                link = item.get('link')
                print(f"{i}. {basliq}")
                print(f"   🔗 Link: {link}\n")
        else:
            print("\n Təəssüf ki, heç bir fayl tapılmadı.")
            
    except Exception as e:
        if "403" in str(e):
            print("\n XƏTA: API hələ aktiv deyil və ya limit bitib.")
        else:
            print(f"\n Gözlənilməz xəta: {e}")

if __name__ == "__main__":
    print("=" * 40)
    print(" İNTERNET FAYL AXTARIŞ SİSTEMİ")
    print("=" * 40)
    
    axtarilan = input("Nə axtarmaq istəyirsiniz? (məs: Python dərslik): ")
    format = input("Fayl formatı (pdf, docx, rar): ").strip().lower()
    
    internetde_fayl_axtar(axtarilan, format)

#run üçün terminalda: python fayl_tap.py