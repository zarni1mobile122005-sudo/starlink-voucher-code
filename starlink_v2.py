import sys
import time
import random
import string

# အဝိုင်းလည်မယ့် ပုံစံလေးများ
spinner = ['|', '/', '-', '\\']

def generate_code(length=12):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def run_search():
    found_codes = []
    
    print("\n[+] Starlink Voucher Searching System Initializing...")
    time.sleep(1)
    
    try:
        while True:
            # Loading Spinner အဝိုင်းလည်တဲ့အပိုင်း
            for _ in range(15): # စက္ကန့်အနည်းငယ်ကြာ ရှာနေတဲ့ပုံစံလုပ်မယ်
                for s in spinner:
                    sys.stdout.write(f'\r[*] Searching for valid codes... {s} ')
                    sys.stdout.flush()
                    time.sleep(0.1)
            
            # Code အသစ်တစ်ခု ရှာတွေ့တဲ့ပုံစံ
            new_code = generate_code()
            found_codes.append(new_code)
            
            # မျက်နှာပြင်ကို ရှင်းပြီး အသစ်ပြန်ပြခြင်း
            print("\n" + "="*45)
            print(f"✅ NEW VOUCHER FOUND: {new_code}")
            print("="*45)
            
            print("\n--- [ HISTORY OF RECENT CODES ] ---")
            # နောက်ဆုံးရထားတဲ့ Code ၅ ခုကိုပဲ ပြပေးမယ် (List မရှည်သွားအောင်)
            for c in found_codes[-5:]:
                print(f" > {c}")
            
            print("\n" + "-"*45)
            time.sleep(1) # ခဏနားပြီး နောက်တစ်ခု ထပ်ရှာမယ်

    except KeyboardInterrupt:
        print("\n\n[!] Search Stopped by User.")
        print(f"Total Codes Found during this session: {len(found_codes)}")

if __name__ == "__main__":
    run_search()
