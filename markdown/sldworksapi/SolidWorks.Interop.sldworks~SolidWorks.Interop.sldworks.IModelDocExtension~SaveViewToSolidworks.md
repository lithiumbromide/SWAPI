---
title: "SaveViewToSolidworks Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SaveViewToSolidworks"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveViewToSolidworks.html"
---

# SaveViewToSolidworks Method (IModelDocExtension)

Saves the specified named view of this model to SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveViewToSolidworks( _
   ByVal ViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ViewName As System.String
Dim value As System.Boolean

value = instance.SaveViewToSolidworks(ViewName)
```

### C#

```csharp
System.bool SaveViewToSolidworks(
   System.string ViewName
)
```

### C++/CLI

```cpp
System.bool SaveViewToSolidworks(
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Custom view name

### Return Value

True if named view successfully saved, false if not

## VBA Syntax

See [ModelDocExtension::SaveViewToSolidworks](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SaveViewToSolidworks.html).

## Examples

'VBA

Option Explicit

Sub main()

Dim swApp As SldWorks.SldWorks

Set swApp = Application.SldWorks

Dim swModel As ModelDoc2

Set swModel = swApp.**ActiveDoc**

swModel.ViewRotateplusz

swModel.**GraphicsRedraw2**

Dim newName As String

newName = Format(Now, "YYYYMMDD-hhmmss")

Dim bResult As Boolean

swModel.**NameView** newName

bResult = swModel.**Extension**.**SaveViewToSolidworks**(newName)

Debug.Print "Saved view to SOLIDWORKS as """ & newName & """ == " & bResult

End Sub

## Remarks

For more information, read **SOLIDWORKS Design user-interface help > Detailing and Drawings > Drawings > Standard Drawing Views > Adding Named Views**.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
