---
title: "IEdmBomMgr3 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr3"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html"
---

# IEdmBomMgr3 Interface

Allows you to add a SOLIDWORKS Bill of Materials (BOM) to a non-SOLIDWORKS document. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBomMgr3
   Inherits IEdmBomMgr, IEdmBomMgr2
```

### C#

```csharp
public interface IEdmBomMgr3 : IEdmBomMgr, IEdmBomMgr2
```

### C++/CLI

```cpp
public interface class IEdmBomMgr3 : public IEdmBomMgr, IEdmBomMgr2
```

## Examples

//C# console application:

// Preconditions:

// 1. Start Microsoft Visual Studio.
// 2. Click **File > New > Project > C#, Windows, Console > Console App**.
// 3. Type AddBomCSharp in **Project name**.
// 4. For **Location**, click **...** and navigate to the folder where to create the project.
// 5. Click **Next**.
// 6. Select **Framework**.
// 7. Click **Create**.
// 8. [Add dependencies and safely pass arrays of structures](file:///E:/APIHelp_SP03/Src/DOCUMENT!X/NET/epdmapi/AddDependencies.htm).
// 9. Replace the code in **Program.cs** with the code below.
//10. Change the namespace to match your setup.
//11. Change the userName, vaultName, swBom.RefDocID, swBom.RefCfgs, swBom.SheetName,
// AddSWBom method parameters, and swRow property assignmentsin the code
// to match your vault and the document to which you want to add this BOM.
//12. Click **Debug > Start Debugging** or press F5.

// Postconditions: Press a key when prompted in the console.

//---------------------------------------------------------------------------

using System;

using System.Collections.Generic;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using EPDM.Interop.epdm;

using EPDM.Interop.EPDMResultCode;

using System.Windows.Forms;

namespace SPR_1207428

{

class Program

{

const int LVCFMT_CENTER = 2;

const int LVCFMT_RIGHT = 1;

static string userName = "Admin";

static string vaultName = "2022_A1_B291";

static void Main(string[] args)

{

StringBuilder sb = new StringBuilder();

try

{

sb.AppendFormat("UserName: {0}", userName).AppendLine();

sb.AppendFormat("VaultName: {0}", vaultName).AppendLine();

IEdmVault11 vault = (IEdmVault11)(new EdmVault5());

if (!vault.IsLoggedIn)

vault.Login(userName, "", vaultName);

IEdmBomMgr3 bomMgr = (IEdmBomMgr3)vault.**CreateUtility**(EdmUtility.EdmUtil_BomMgr);

IEdmSWBom swBom = bomMgr.**CreateEmptySWBom**();

swBom.**Name** = "Custom SWBom 7";

swBom.**TableType** = 0;

swBom.**StartNumber** = 1;

swBom.**IncrementNumber** = 1;

swBom.**RefCfgs** = "Default";

swBom.**RefDocID** = 1553;

swBom.**SheetName** = "Sheet1";

IEdmSWBomColumn swColTmp;

swColTmp = swBom.**InsertColumn**(0, "PART NUMBER");

swColTmp.**Flags** = LVCFMT_CENTER;

swColTmp.**Width** = 120;

swColTmp.**Type** = 8;

swColTmp = swBom.**InsertColumn**(1, "DESCRIPTION");

swColTmp.**Flags** = LVCFMT_CENTER;

swColTmp.**Width** = 231;

swColTmp.**CustomPropName** = "Description";

swColTmp = swBom.**InsertColumn**(2, "WEIGHT");

swColTmp.**Flags** = LVCFMT_CENTER;

swColTmp.Width = 71;

swColTmp.**CustomPropName** = "Weight";

swColTmp = swBom.**InsertColumn**(3, "VENDOR");

swColTmp.**Flags** = LVCFMT_CENTER;

swColTmp.**Width** = 132;

swColTmp.**CustomPropName** = "Vendor";

swColTmp = swBom.**InsertColumn**(4, "QTY.");

swColTmp.**Flags** = LVCFMT_RIGHT;

swColTmp.**Width** = 71;

swColTmp.**Type** = 6;

swColTmp = swBom.**InsertColumn**(0, "ITEM NO."); // insert at first position; reorders previous indexing

swColTmp.**Flags** = LVCFMT_CENTER;

swColTmp.**Width** = 71;

swColTmp.**Type** = 7;

IEdmSWBomRow swRow = swBom.**InsertRow**(0);

swRow.**DocID** = 1556;

swRow.**Configuration** = "Default";

swRow.**Version** = 1;

swRow.**ProjectID** = 7;

//swRow.ComponentRep = "SW-100200-2<Default>@Bill of Materials1/SW-100217-1<Default>@SW-100200/SW-201831-1<Default>@SW-100217";

swBom.**GetCell**(0, 0).Text = "1"; //Item number

swBom.**GetCell**(0, 1).Text = "SW-201831"; //Part number

swBom.**GetCell**(0, 2).Text = "BASE"; //Description

swBom.**GetCell**(0, 3).Text = "3696.33"; //Weight

swBom.**GetCell**(0, 5).Text = "1"; //Quantity

//Add the new SOLIDWORKS BOM to document with ID=1553 and Version=9

bomMgr.**AddSWBom**(1553, 7, 9, (EdmSWBom)swBom);

sb.AppendFormat("{0} sucessfully added.", swBom.**Name**).AppendLine();

}

catch (System.Runtime.InteropServices.COMException ex)

{

var errorType = typeof(EdmResultErrorCodes_e);

if (Enum.IsDefined(errorType, ex.ErrorCode))

sb.AppendFormat("Edm error occurred: {0}", Enum.GetName(errorType, ex.ErrorCode)).AppendLine();

else

sb.AppendLine("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message);

}

catch (Exception ex)

{

sb.AppendFormat("Error occurred: {0}", ex.Message).AppendLine();

}

Console.WriteLine(sb.ToString());

Console.WriteLine("Please press any key to exit");

Console.ReadKey();

}

}

}

## Remarks

This interface:

- extends [IEdmBomMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html) by providing the ability to:

  - create a SOLIDWORKS BOM with rows and columns not tied to a fixed layout.
  - add a SOLIDWORKS BOM to a non-SOLIDWORKS document in the vault.

- is extended by [IEdmBomMgr4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4.html).

To access this interface, call IEdmVault7::CreateUtility with eType = [EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BomMgr and then cast the returned object to IEdmBomMgr3.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBomMgr3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3_members.html)
[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
