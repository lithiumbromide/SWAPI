---
title: "Getting Started"
project: "eDrawings API Help"
interface: ""
member: ""
kind: "topic"
source: "emodelapi/GettingStarted-emodelapi.html"
---

# Getting Started

##### Using the eDrawings ActiveX control

The eDrawings API is implemented as a Microsoft ActiveX control.

###### Prerequisites

- Microsoft Visual Studio is installed
- eDrawings 20`nn` is installed
- **eDrawings Example.zip** is available

###### Modify SOLIDWORKS eDrawings C# example

Use the 3DSupport App to ask SOLIDWORKS API Support to provide the **eDrawings Example.zip**, which includes two Microsoft Visual Studio projects written in C# that you will modify in the following two procedures.

Procedure 1: Modify the SOLIDWORKS eDrawings Host Control C# example

1. Unzip and extract **eDrawingHostControl source project.zip**, located in the HostControl folder.
2. Open **eDrawingHostControl.csproj** in Microsoft Visual Studio and convert the project.
3. Click **Show All Files** in the Solution Explorer and expand **References**.
4. Locate and update the existing reference to **Interop.EModelView.dll** as necessary.
5. Click **Project > eDrawingHostControl Properties**.

  1. Click **Build** and change Platform target to x64.
  2. Click **Application**, change Target framework as needed`,` and click **Yes**.
6. Start debugging.
7. Click **Yes** when informed of different versions.
8. Click **Close** on the form.
9. Save and exit the project.

Procedure 2: Modify the SOLIDWORKS eDrawings C# example

1. Open **eDrawingsExample.csproj** in Microsoft Visual Studio and convert the project.

  NOTE: This project is located in the eDrawingsExample folder.
2. Click **Project > eDrawingsExample Properties > Build** and change Platform target to x64.
3. Click **Show All Files** in the Solution Explorer and expand **References**.
4. Remove the existing eDrawingHostControl reference and add a reference to **\bin\Debug\eDrawingHostControl.dll**, which you created in the [first procedure](#first). Check the date on the file to ensure that you are adding the DLL that you created.
5. Locate and update the existing reference to **Interop.****EModelView.dll** as necessary.
6. Change the name of the SOLIDWORKS or eDrawings file to open in **Form1.cs** to a file that exists on your computer.
7. Start debugging.
8. Click **Yes** when informed of different versions.
9. Click Open to open the file.
10. Click **OK** to close the message box.
11. Close the form, save, and exit the project.

###### Create a C# eDrawings project

1. Modify the SOLIDWORKS eDrawings Host Control C# example. See the [first procedure](#first).
2. Open Microsoft Visual Studio.
3. Create a C# Windows Forms Application project and name it WindowsFormsApplication1.
4. Click **Project > WindowsFormsApplication1 Properties**.

  1. Click **Build** and change Platform target to x64.
  2. Click **Application**, change Target framework as needed`,` and click **Yes**.
5. Click **Show All Files** in the Solution Explorer and expand **References**.
6. Locate and add a reference to **Interop.****EModelView.dll**.
7. Add a reference to **\bin\Debug\eDrawingHostControl.dll**, which you created in the [first procedure](#first). Check the date on the file to ensure that you are adding the DLL that you created.
8. Double-click **Form1.cs** in the Solution Explorer to show the form.
9. Click **View > Toolbox**, expand **All Windows Forms**, and drag a button onto the form.
10. Double-click the button.
11. Replace the code in **Form1.cs** with this code:

  ```
  using System.Data;
  using System.Drawing;
  using System.Linq;
  using System.Text;
  using System.Threading.Tasks;
  using System.Windows.Forms;
  using eDrawingHostControl;
  ```

  ```
  namespace WindowsFormsApplication1
  {
      public partial class Form1 : Form
      {
          eDrawingHostControl.eDrawingControl ctrl = null;
  ```

  ```
          public Form1()
  ```

  ```
          {
              InitializeComponent();
              if (null == ctrl)
              {
                  ctrl = new eDrawingControl();
              }
  ```

  ```
              this.Controls.Add(ctrl);
  ```

  ```
          }
  ```

  ```
          private void Form1_Load(object sender, System.EventArgs e)
          {
          }
  ```

  ```
          private void button1_Click(object sender, System.EventArgs e)
          {
              if(ctrl != null)
              {
              ctrl.Location = new Point(0,0);
              ctrl.Size = new System.Drawing.Size(this.Size.Width,this.Size.Height);
              ctrl.eDrawingControlWrapper.OpenDoc("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2024\\samples\\tutorial\\EDraw\\claw\\claw.sldprt", false, false, false, "");
              }
          }
      }
  }
  ```
12. Start debugging to display the form.
13. Click **button1**.
  If the file specified in button1_Click exists on your computer, it is displayed. If that file does not exist on your computer, then close the form, edit the file's path and file name in **Form1.cs** to specify a SOLIDWORKS or eDrawings file on your computer, and repeat steps 13 and 14.
14. Close the form and save the project.

You can also ask SOLIDWORKS API Support to give you the sample, **Add eModelViewControl to a Windows.Forms Application at runtime (eDrawings ActiveX Control)**, which shows how to add instances of the eDrawings ActiveX control IEModelViewControl to a Window.Forms application at runtime.

###### Instantiating the eDrawings Control

You can instantiate the eDrawings control using version-specific or version-independent class IDs (CLSIDs).

To get your version-specific eDrawings control's CLSIDs:

1. Run the Windows Registry editor, regedit.
2. Expand HKEY_CLASSES_ROOT.
3. Locate and double-click EModelView.EModelViewControl.`nn`, where `nn` is the 2-digit release year of the version of eDrawings installed on your computer. For example, if eDrawings 2024 is installed on your computer, then nn is 24.
4. Click CLSID. Make note of the CLSID.
5. Locate and double-click EModelViewMarkup.EModelMarkupControl.nn.
6. Click CLSID. Make note of the CLSID.
7. Exit regedit.

The version-independent eDrawings CLSIDs are:

- EModelNonVersionSpecificViewControl = 22945A69-1191-4DCF-9E6F-409BDE94D101
- EModelNonVersionSpecificMarkupControl = 5BBBC05A-BD4D-4e3b-AD5B-51A79DFC522F

SOLIDWORKS recommends that you use version-specific CLSIDs, because Microsoft Visual Studio selects them by default. However, because CLSIDs are version specific, with each new release of eDrawings you must edit:

- your application.
- any HTML pages that reference version-specific CLSIDs.

Although you do not need to edit your application when working with multiple versions of eDrawings when using the version-independent CLSID, if your application uses a newer API than present in an older version of eDrawings installed by your user, your application will not work properly. This scenario can be difficult to debug remotely, especially with HTML applications.

[Back to top](GettingStarted-emodelapi.html#top)
