---
title: "GetModelBreakViewNames Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetModelBreakViewNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelBreakViewNames.html"
---

# GetModelBreakViewNames Method (IModelDocExtension)

Gets the names and number of the Model Break Views in the current configuration of the active model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelBreakViewNames( _
   ByRef Views As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Views As System.Object
Dim value As System.Integer

value = instance.GetModelBreakViewNames(Views)
```

### C#

```csharp
System.int GetModelBreakViewNames(
   out System.object Views
)
```

### C++/CLI

```cpp
System.int GetModelBreakViewNames(
   [Out] System.Object^ Views
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Views`: Names of Model Break Views

### Return Value

Number of Model Break Views

## VBA Syntax

See [ModelDocExtension::GetModelBreakViewNames](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetModelBReakViewNames.html).

## Examples

[Get Names and Show Model Break Views (C#)](Get_Names_and_Show_Model_Break_Views_Example_CSharp.htm)
[Get Names and Show Model Break Views (VB.NET)](Get_Names_and_Show_Model_Break_Views_Example_VBNET.htm)
[Get Names and Show Model Break Views (VBA)](Get_Names_and_Show_Model_Break_Views_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ShowModelBreakView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowModelBreakView.html)
[IView3D::ModelBreakViewName Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D~ModelBreakViewName.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
