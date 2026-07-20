---
title: "IEdmBomMgr3 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr3"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html"
---

# IEdmBomMgr3 Interface

Allows you to add a SOLIDWORKS Bill of Materials (BOM) to a non-SOLIDWORKS document.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

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

//----------------------------------------------------------------------------

// Preconditions:

// 1. Start Microsoft Visual Studio.

// a. Click File > New > Project > Visual C# > Console Applicat ion.

// b. Type Search in Name.

// c. Click Browse and navigate to the folder where to create the project.

// d. Click OK .

// e. Click Show All Files in the Solution Explorer toolbar and expand

// Program.cs in the Solution Explorer.

// f. Replace the code in Program.cs with the code below.

// g. Change the namespace to match your setup.

// 2. Add EPDM.Interop.epdm.dll and EPDM.Interop.EPDMResultCode as references // (right-click the projectname in the Solution Explorer, click Add Reference , click

// Assemblies > Framework in the left-side panel, browse to the top folder of

// your SOLIDWORKS PDM Professional installation, locate and select

// EPDM.Interop.epdm.dll , click Open , click Add , and click Close ).

// 3. Change the userName, vaultName, swBom.RefDocID, swBom.RefCfgs, swBom.SheetName, // AddSWBom method parameters, and swRow property assignmentsin the code // to match your vault and the document to which you want to add this BOM.

// 4. Click Debug > Start Debugging or press F5.

//

// Postconditions: Press a key when prompted in the console.

//----------------------------------------------------------------------------

//Program.cs

usingSystem;

usingSystem.Collections.Generic;

usingSystem.Linq;

usingSystem.Text;

usingSystem.Threading.Tasks;

usingEPDM.Interop.epdm;

usingEPDM.Interop.EPDMResultCode;

usingSystem.Windows.Forms;

namespaceSPR_1207428

{

classProgram

{

constintLVCFMT_CENTER = 2;

constintLVCFMT_RIGHT = 1;

staticstringuserName ="Admin";

staticstringvaultName ="2022_A1_B291";

staticvoidMain(string[] args)

{

StringBuilder sb =newStringBuilder();

try

{

sb.AppendFormat("UserName: {0}", userName).AppendLine();

sb.AppendFormat("VaultName: {0}", vaultName).AppendLine();

IEdmVault11 vault = (IEdmVault11)(newEdmVault5());

if(!vault.IsLoggedIn)

vault.Login(userName,"", vaultName);

IEdmBomMgr3 bomMgr = (IEdmBomMgr3)vault. CreateUtility (EdmUtility.EdmUtil_BomMgr);

IEdmSWBom swBom = bomMgr. CreateEmptySWBom ();

swBom. Name ="Custom SWBom 7";

swBom. TableType = 0;

swBom. StartNumber = 1;

swBom. IncrementNumber = 1;

swBom. RefCfgs ="Default";

swBom. RefDocID = 1553;

swBom. SheetName ="Sheet1";

IEdmSWBomColumn swColTmp;

swColTmp = swBom. InsertColumn (0,"PART NUMBER");

swColTmp. Flags = LVCFMT_CENTER;

swColTmp. Width = 120;

swColTmp. Type = 8;

swColTmp = swBom. InsertColumn (1,"DESCRIPTION");

swColTmp. Flags = LVCFMT_CENTER;

swColTmp. Width = 231;

swColTmp. CustomPropName ="Description";

swColTmp = swBom. InsertColumn (2,"WEIGHT");

swColTmp. Flags = LVCFMT_CENTER;

swColTmp.Width = 71;

swColTmp. CustomPropName ="Weight";

swColTmp = swBom. InsertColumn (3,"VENDOR");

swColTmp. Flags = LVCFMT_CENTER;

swColTmp. Width = 132;

swColTmp. CustomPropName ="Vendor";

swColTmp = swBom. InsertColumn (4,"QTY.");

swColTmp. Flags = LVCFMT_RIGHT;

swColTmp. Width = 71;

swColTmp. Type = 6;

swColTmp = swBom. InsertColumn (0,"ITEM NO.");// insert at first position; reorders previous indexing

swColTmp. Flags = LVCFMT_CENTER;

swColTmp. Width = 71;

swColTmp. Type = 7;

IEdmSWBomRow swRow = swBom. InsertRow (0);

swRow. DocID = 1556;

swRow. Configuration ="Default";

swRow. Version = 1;

swRow. ProjectID = 7;

//swRow.ComponentRep = "SW-100200-2<Default>@Bill of Materials1/SW-100217-1<Default>@SW-100200/SW-201831-1<Default>@SW-100217";

swBom. GetCell (0, 0).Text ="1"; //Item number

swBom. GetCell (0, 1).Text ="SW-201831"; //Part number

swBom. GetCell (0, 2).Text ="BASE"; //Description

swBom. GetCell (0, 3).Text ="3696.33"; //Weight

swBom. GetCell (0, 5).Text ="1"; //Quantity //Add the new SOLIDWORKS BOM to document with ID=1553 and Version=9

bomMgr. AddSWBom (1553, 7, 9, (EdmSWBom)swBom);

sb.AppendFormat("{0} sucessfully added.", swBom. Name ).AppendLine();

}

catch(System.Runtime.InteropServices.COMException ex)

{

varerrorType =typeof(EdmResultErrorCodes_e);

if(Enum.IsDefined(errorType, ex.ErrorCode))

sb.AppendFormat("Edm error occurred: {0}", Enum.GetName(errorType, ex.ErrorCode)).AppendLine();

else

sb.AppendLine("HRESULT = 0x"+ ex.ErrorCode.ToString("X") +" "+ ex.Message);

}

catch(Exception ex)

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

- extends

  [IEdmBomMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html)

  by providing the ability to:

  - create a SOLIDWORKS BOM with rows and columns not tied to a fixed layout.
  - add a SOLIDWORKS BOM to a non-SOLIDWORKS document in the vault.

- is extended by

  [IEdmBomMgr4](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4.html)

  .

To access this interface, call IEdmVault7::CreateUtility with eType =[EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BomMgr and then cast the returned object to IEdmBomMgr3.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBomMgr3 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
