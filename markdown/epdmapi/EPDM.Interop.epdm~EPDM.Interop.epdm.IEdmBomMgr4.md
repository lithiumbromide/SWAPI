---
title: "IEdmBomMgr4 Interface"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomMgr4"
member: ""
kind: "interface"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4.html"
---

# IEdmBomMgr4 Interface

Allows you to access the Bill of Materials (BOM) layouts installed in a vault.

NOTE:

Click the

Members

link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic

```vb
Public Interface IEdmBomMgr4
   Inherits IEdmBomMgr, IEdmBomMgr2, IEdmBomMgr3
```

### C#

```csharp
public interface IEdmBomMgr4 : IEdmBomMgr, IEdmBomMgr2, IEdmBomMgr3
```

### C++/CLI

```cpp
public interface class IEdmBomMgr4 : public IEdmBomMgr, IEdmBomMgr2, IEdmBomMgr3
```

## Examples

Tailor the[IEdmBomMgr2](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr2.html)C# example to use this interface by replacing its GetBOM_Click function with:

publicvoidGetBOM_Click(System.Object sender, System.EventArgs e)

{

try

{

IEdmVault11 vault2 =null;

if(vault1 ==null)

{

vault1 =newEdmVault5();

}

vault2 = (IEdmVault11)vault1;

if(!vault1.IsLoggedIn)

{

vault1.LoginAuto(VaultsComboBox.Text,this.Handle.ToInt32());

}

if(aFile !=null)

{

// Get named BOMs and their versions for the selected file

EdmBomInfo[] derivedBOMs =null;

aFile.GetDerivedBOMs(outderivedBOMs);

intarrSize = 0;

EdmBomVersion[] ppoVersions =null;

inti = 0;

intj = 0;

intid = 0;

stringstr ="";

stringverstr ="";

intverArrSize = 0;

arrSize = derivedBOMs.Length;

intuserID = 0;

boolcanSeeLayout =false;

userID = vault2.GetLoggedInWindowsUserID(vault2.Name);

while(i < arrSize)

{

id = derivedBOMs[i].mlBomID;

bom = (IEdmBom)vault2.GetObject(EdmObjectType.EdmObject_BOM, id);

str ="Named BOM: "+ derivedBOMs[i].mbsBomName +"\r\n"+"Type of BOM as defined in EdmBomType: "+ derivedBOMs[i].meType +"\\n"+"Check-out user: "+ bom.CheckOutUserID +"\r\n"+"Current state: "+ bom.CurrentState.Name +"\r\n"+"Current version: "+ bom.CurrentVersion +"\r\n"+"ID: "+ bom.FileID +"\r\n"+"Is checked out: "+ bom.IsCheckedOut;

MessageBox.Show(str);

bom.GetVersions(outppoVersions);

verArrSize = ppoVersions.Length;

while(j < verArrSize)

{

verstr ="BOM version: "+"\r\n"+"Type as defined in EdmBomVersionType: "+ ppoVersions[j].meType +"\r\n"+"Version number: "+ ppoVersions[j].mlVersion +"\r\n"+"Date: "+ ppoVersions[j].moDate +"\r\n"+"Label: "+ ppoVersions[j].mbsTag +"\r\n"+"Comment: "+ ppoVersions[j].mbsComment;

MessageBox.Show(verstr);

j = j + 1;

}

i = i + 1;

}

// Get a BOM view with the specified layout

bomMgr = (IEdmBomMgr2)vault2.CreateUtility(EdmUtility.EdmUtil_BomMgr);

EdmBomLayout2[] ppoRetLayouts =null;

EdmBomLayout2 ppoRetLayout =default(EdmBomLayout2);

bomMgr.GetBomLayouts2(outppoRetLayouts);

i = 0;

arrSize = ppoRetLayouts.Length;

str ="";

while(i < arrSize)

{

ppoRetLayout = ppoRetLayouts[i];

canSeeLayout = bomMgr.CanSeeBomLayout(userID, ppoRetLayout.mlLayoutID);

bomMgr4 = (IEdmBomMgr4)bomMgr;

EdmBomDefaultSetting _bomDefSetting;

_bomDefSetting = bomMgr4. GetBomDefaultSetting (ppoRetLayout.mlLayoutID);

str ="";

switch(_bomDefSetting. mlBomDisplayType )

{

case1: str ="BOM display type is indented";break;

case2: str ="BOM display Type is parts only";break;

case3: str ="BOM display type is top level only";break;

case4: str ="BOM display type is Flattened";break;

}

MessageBox.Show(str);

str ="BOM Layout "+ i +": "+ ppoRetLayout.mbsLayoutName +"\r\n"+"ID: "+ ppoRetLayout.mlLayoutID;

str = str +" Logged-in user can see this layout? "+ canSeeLayout;

if(ppoRetLayout.mbsLayoutName =="BOM")

{

bomView = (IEdmBomView3)aFile.GetComputedBOM(ppoRetLayout.mbsLayoutName, 0,"@", (int)EdmBomFlag.EdmBf_AsBuilt + (int)EdmBomFlag.EdmBf_ShowSelected);

}

MessageBox.Show(str);

i = i + 1;

}

// Display BOM view row and column information

object[] ppoRows =null;

IEdmBomCell ppoRow =default(IEdmBomCell);

bomView.GetRows(outppoRows);

i = 0;

arrSize = ppoRows.Length;

str ="";

while(i < arrSize)

{

ppoRow = (IEdmBomCell)ppoRows[i];

str ="BOM Row "+ i +": "+"\r\n"+"Item ID: "+ ppoRow.GetItemID() +"\r\n"+"Path name: "+ ppoRow.GetPathName() +"\r\n"+"Tree level: "+ ppoRow.GetTreeLevel() +"\r\n"+" Is locked? "+ ppoRow.IsLocked();

MessageBox.Show(str);

i = i + 1;

}

EdmBomColumn[] ppoColumns =null;

bomView.GetColumns(outppoColumns);

i = 0;

arrSize = ppoColumns.Length;

str ="";

while(i < arrSize)

{

str ="BOM Column "+ i +": "+"\r\n"+"Header: "+ ppoColumns[i].mbsCaption +"\r\n"+"Column type as defined in EdmBomColumnType: "+ ppoColumns[i].meType +"\r\n"+"ID: "+ ppoColumns[i].mlColumnID +"\r\n"+"Flags: "+ ppoColumns[i].mlFlags +"\r\n"+"Variable ID: "+ ppoColumns[i].mlVariableID +"\r\n"+"Variable type as defined in EdmVariableType: "+ ppoColumns[i].mlVariableType +"\r\n"+"Column width: "+ ppoColumns[i].mlWidth;

MessageBox.Show(str);

i = i + 1;

}

SaveBOM.Enabled =true;

}

}

catch(System.Runtime.InteropServices.COMException ex)

{

MessageBox.Show("HRESULT = 0x"+ ex.ErrorCode.ToString("X") +" "+ ex.Message);

}

catch(Exception ex)

{

MessageBox.Show(ex.Message);

}

}

## Remarks

This interface:

- extends

  [IEdmBomMgr3](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr3.html)

  by providing the ability to get a computed BOM's default view settings as specified in the Conisio Admin tool.

To access this interface, call IEdmVault7::CreateUtility with eType =[EdmUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUtility.html).EdmUtil_BomMgr and then cast the returned object to IEdmBomMgr4.

## Accessors

[IEdmVault7::CreateUtility](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault7~CreateUtility.html)

## See Also

[IEdmBomMgr4 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomMgr4_members.html)

[EPDM.Interop.epdm Namespace](EPDM.Interop.epdm~EPDM.Interop.epdm_namespace.html)
