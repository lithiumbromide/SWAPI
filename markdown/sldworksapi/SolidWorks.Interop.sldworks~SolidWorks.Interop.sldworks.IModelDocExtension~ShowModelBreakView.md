---
title: "ShowModelBreakView Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ShowModelBreakView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowModelBreakView.html"
---

# ShowModelBreakView Method (IModelDocExtension)

Gets whether to show or hide the specified Model Break View in the current configuration of the active model.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowModelBreakView( _
   ByVal ShowView As System.Boolean, _
   ByVal ViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ShowView As System.Boolean
Dim ViewName As System.String
Dim value As System.Boolean

value = instance.ShowModelBreakView(ShowView, ViewName)
```

### C#

```csharp
System.bool ShowModelBreakView(
   System.bool ShowView,
   System.string ViewName
)
```

### C++/CLI

```cpp
System.bool ShowModelBreakView(
   System.bool ShowView,
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowView`: True to show the Model Break View, false to hide it
- `ViewName`: Name of Model Break View to show or hide

### Return Value

True if the method executed, false if it did not

## VBA Syntax

See [ModelDocExtension::ShowModelBreakView](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ShowModelBreakView.html).

## Examples

[Get Names and Show Model Break Views (C#)](Get_Names_and_Show_Model_Break_Views_Example_CSharp.htm)
[Get Names and Show Model Break Views (VB.NET)](Get_Names_and_Show_Model_Break_Views_Example_VBNET.htm)
[Get Names and Show Model Break Views (VBA)](Get_Names_and_Show_Model_Break_Views_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetModelBreakViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetModelBreakViewNames.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
