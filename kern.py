import os
import pyautogui
from time import sleep


def ker():
    os.system("apt update")
    print("[+] update")
    os.system("apt upgrade -y")
    print("[+] upgrade")
    os.system("apt dist-upgrade -y")
    print("[+] dist-upgrade")
    os.system("apt install git -y")
    print("[+] git")
    os.system("apt-get install adb android-sdk-platform-tools git-core ark tar make gnupg flex bc bison gperf build-essential zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev libgl1-mesa-dev libxml2-utils xsltproc unzip -y")
    print("[+] apt-get")
    os.system("mkdir kernel_dev")
    os.system("cd kernel_dev")
    print("[+] kernel_dev")
    os.system("git clone https://github.com/lineage-x2-devs/android_kernel_leeco_msm8996/ -b lineage-16.0 kernel_lineageos-16_leeco")
    os.system("wget https://releases.linaro.org/components/toolchain/binaries/4.9-2017.01/aarch64-linux-gnu/gcc-linaro-4.9.4-2017.01-x86_64_aarch64-linux-gnu.tar.xz")
    os.system("tar xf gcc-linaro-4.9.4-2017.01-x86_64_aarch64-linux-gnu.tar.xz")
    print("[+] tar xf")
    x, y = pyautogui.locateCenterOnScreen("File.png")
    pyautogui.doubleClick(x, y)
    sleep(30)
    pyautogui.hotkey("ctrl", "h")
    x, y = pyautogui.locateCenterOnScreen("bashrc.png")
    pyautogui.doubleClick(x, y)
    sleep(30)
    pyautogui.hotkey("ctrl", "end")
    pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.press("enter")
    sleep(1)
    pyautogui.typewrite("export ARCH=arm64", interval=0.2)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.typewrite("export SUBARCH=arm64", interval=0.2)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.typewrite("export CROSS_COMPILE=/root/kernel_dev/gcc-linaro-4.9.4-2017.01-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-", interval=0.2)
    sleep(1)
    pyautogui.hotkey("ctrl", "s")
    x, y = pyautogui.locateCenterOnScreen("clse.png")
    pyautogui.click(x, y)
    x, y = pyautogui.locateCenterOnScreen("clse.png")
    pyautogui.click(x, y)
    os.system("cd ..")
    os.system("source /root/.bashrc")
    os.system("echo $CROSS_COMPILE")
    os.system("cd kernel_dev")
    os.system("cd kernel_lineageos-16_leeco")
    os.system("wget http://patches.aircrack-ng.org/mac80211.compat08082009.wl_frag+ack_v1.patch")
    os.system("patch -p1 < mac80211.compat08082009.wl_frag+ack_v1.patch")
    os.system("make clean")
    os.system("make mrproper")
    os.system("make lineage_x2_defconfig")
    print("[+] Всё заебись, пиши в лс")


ui = input("хуярим?(y/n): ")

if ui == "y":
    ker()
