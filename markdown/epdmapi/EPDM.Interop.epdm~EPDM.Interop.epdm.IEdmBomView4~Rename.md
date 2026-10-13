---
title: "Rename Method (IEdmBomView4)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomView4"
member: "Rename"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView4~Rename.html"
---

# Rename Method (IEdmBomView4)

Renames this named BOM.

## Syntax

### Visual Basic

```vb
Sub Rename( _
   ByVal bsFileName As System.String _
)
```

### C#

```csharp
void Rename(
   System.string bsFileName
)
```

### C++/CLI

```cpp
void Rename(
   System.String^ bsFileName
)
```

### Parameters

- `bsFileName`: New file name of named BOM

## Examples

// Preconditions:

// 1. Start Microsoft Visual Studio.
// 2. Click **File > New > Project > C#, Windows, Console > Console App**.
// 3. Type RenameBomCSharp in **Project name**.
// 4. For **Location**, click **...** and navigate to the folder where to create the project.
// 5. Click **Next**.
// 6. Select **Framework**.
// 7. Click **Create**.
// 8. [Add dependencies and safely pass arrays of structures](file:///E:/APIHelp_SP03/Src/DOCUMENT!X/NET/epdmapi/AddDependencies.htm).
// 9. Copy the code below to Program.cs.
//10. Change the namespace to match your project name.
//11. Add an assembly with a named BOM to your vault.
//12. Ensure that parameters of Login, and GetFileFromPath match your vault.
//13. Modify the Rename method’s parameter to rename your assembly’s named BOM.

//

//Postconditions:

//1. Refresh your vault view.
//2. Select the assembly with the named BOM in the vault.
//3. Observe the renamed BOM in the BOM dropdown on the Bill of Materials tab.

//Program.cs:

using System;

using EPDM.Interop.epdm;
using EPDM.Interop.EPDMResultCode;

using System.Windows.Forms;

namespace RenameBomCSharp

{

class Program

{

static IEdmVault5 vault1 = null;

static IEdmFile7 aFile;

static string userName = "Admin";

static void Main(string[] args)

{

try

{

vault1 = new EdmVault5();

if (!vault1.**IsLoggedIn**)

vault1.**Login**(userName, "password", "JEB12");

IEdmVault7 vault7 = (IEdmVault7)vault1;

IEdmFolder5 ppoRetParentFolder;

aFile = (IEdmFile7)vault1.**GetFileFromPath**("C:\\Users\\J4M\\Desktop\\JEB12\\test3.sldasm", out ppoRetParentFolder);

EdmBomInfo[] derivedBOMs = null;

aFile.**GetDerivedBOMs**(out derivedBOMs);

int bomId = derivedBOMs[0].**mlBomID**;

IEdmBom bom = (IEdmBom)vault7.**GetObject**(EdmObjectType.EdmObject_BOM, bomId);

EdmBomVersion[] ppoVersions = null;

bom.**GetVersions**(out ppoVersions);

IEdmBomView4 bomView = (IEdmBomView4)bom.**GetView**(ppoVersions[ppoVersions.Length - 1].**mlVersion**);

bomView.**Rename**("test3_renamed.sldasm.1.BOM");

Console.WriteLine("BOM successfully renamed");

Console.WriteLine("Press any key to exit");

Console.ReadKey();

}

catch (System.Runtime.InteropServices.COMException ex)

{

var errorType = typeof(EdmResultErrorCodes_e);

if (Enum.IsDefined(errorType, ex.ErrorCode))

MessageBox.Show(String.Format("Error occurred: {0}", Enum.GetName(errorType, ex.ErrorCode)));

else

MessageBox.Show("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);

}

catch (Exception ex)

{

MessageBox.Show(ex.Message);

}

}

}

}

## Remarks

Named BOMs are saved as:

`file_name`.sld`ext`.`version`.BOM

Be sure to use the correct format when specifying bsFileName. For example, if you get **assembly.sldasm**, then to rename its BOM set bsFileName to:

assembly_renamed.sldasm.1.BOM

## See Also

[IEdmBomView4 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView4.html)
[IEdmBomView4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomView4_members.html)

## Availability

SOLIDWORKS PDM Professional 2022
