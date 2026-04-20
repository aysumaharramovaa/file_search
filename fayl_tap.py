from googleapiclient.discovery import build

# Sənin məlumatların
MY_API_KEY = "AIzaSyC3VUWodhUniS8AnGp4cNAAPhli6mNv-4w"
MY_CX_ID = "0609deef8cd0a4abb"

def internetde_fayl_axtar(movzu, fayl_tipi):
    try:
        # Google xidmətini başladırıq
        service = build("customsearch", "v1", developerKey=MY_API_KEY)
        
        # Axtarış sorğusunu hazırlayırıq (Məsələn: "fizika filetype:pdf")
        tam_sorgu = f"{movzu} filetype:{fayl_tipi}"
        
        # Axtarışı icra edirik
        netice = service.cse().list(q=tam_sorgu, cx=MY_CX_ID).execute()
        
        if 'items' in netice:
            print(f"\n--- '{movzu}' mövzusunda {fayl_tipi} faylları tapıldı ---\n")
            for i, item in enumerate(netice['items'], 1):
                basliq = item.get('title')
                link = item.get('link')
                print(f"{i}. {basliq}")
                print(f"   Yükləmə linki: {link}\n")
        else:
            print("Təəssüf ki, heç bir fayl tapılmadı. Axtarış sözünü dəyişib yenidən yoxlayın.")
            
    except Exception as e:
        print(f"Xəta baş verdi: {e}")
        print("Məsləhət: Google Cloud Console-da 'Custom Search API'-nin aktiv olduğundan əmin olun.")

if __name__ == "__main__":
    print("=== İNTERNET FAYL AXTARIŞ PROQRAMI ===")
    axtarilan = input("Nə axtarmaq istəyirsiniz? (məs: C++ derslik): ")
    format = input("Fayl formatı nə olsun? (pdf, docx, zip, rar): ")
    
    internetde_fayl_axtar(axtarilan, format)