---
title: "InsertBendTable Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "InsertBendTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~InsertBendTable.html"
---

# InsertBendTable Method (IPartDoc)

Creates a bend table annotation for the flat pattern of this sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBendTable( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal StartValue As System.String, _
   ByVal TableTemplate As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim X As System.Double
Dim Y As System.Double
Dim StartValue As System.String
Dim TableTemplate As System.String
Dim value As System.Object

value = instance.InsertBendTable(X, Y, StartValue, TableTemplate)
```

### C#

```csharp
System.object InsertBendTable(
   System.double X,
   System.double Y,
   System.string StartValue,
   System.string TableTemplate
)
```

### C++/CLI

```cpp
System.Object^ InsertBendTable(
   System.double X,
   System.double Y,
   System.String^ StartValue,
   System.String^ TableTemplate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X-coordinate for placement of the bend table
- `Y`: Y-coordinate for placement of the bend table
- `StartValue`: Starting datum tag; a value from A to Z for letter tags; a positive integer for number tags
- `TableTemplate`: Full pathname of the template (e.g., `install_dir`\**lang\**`language\`**bendtable-standard.sldbndtbt**)

### Return Value

[IBendTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation.html)

## VBA Syntax

See [PartDoc::InsertBendTable](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~InsertBendTable.html).

## Examples

'VBA

'*****************************************************

'1. Ensure the specified part and table template exist.
'2. Run the macro.
'3. Inserts a bend table annotation for the flat pattern.
'4. Inspect the graphics area and the Immediate window.

'*****************************************************

Dim swApp As SldWorks.SldWorks
Dim myBendTableAnno As SldWorks.BendTableAnnotation
Dim myBendTable As SldWorks.BendTable
Dim Part As SldWorks.ModelDoc2
Dim boolstatus As Boolean
Dim longstatus As Long, longwarnings As Long
Option Explicit
Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\SMGussetAPI.SLDPRT", 1, 0, "", longstatus, longwarnings)
swApp.ActivateDoc2 "SMGussetAPI.SLDPRT", False, longstatus
Set Part = swApp.ActiveDoc

Set myBendTableAnno = Part.**InsertBendTable**(-4.06616963665726E-02, 6.09432383467686E-02, "A", "install_dir\lang\english\bendtable-standard.sldbndtbt")
Set myBendTable = myBendTableAnno.**BendTable**
Debug.Print "Tag style of the bend table as defined in swBendTableTagStyle_e: " & myBendTable.TagStyle

End Sub

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IBendTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable.html)
[IView::InsertBendTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBendTable.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
