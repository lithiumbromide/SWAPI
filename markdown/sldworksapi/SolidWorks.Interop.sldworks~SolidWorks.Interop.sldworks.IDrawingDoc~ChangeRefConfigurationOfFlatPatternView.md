---
title: "ChangeRefConfigurationOfFlatPatternView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ChangeRefConfigurationOfFlatPatternView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeRefConfigurationOfFlatPatternView.html"
---

# ChangeRefConfigurationOfFlatPatternView Method (IDrawingDoc)

Changes the configuration of the selected flat-pattern view of the specified model.

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeRefConfigurationOfFlatPatternView( _
   ByVal ModelName As System.String, _
   ByVal ConfigName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ConfigName As System.String
Dim value As System.Boolean

value = instance.ChangeRefConfigurationOfFlatPatternView(ModelName, ConfigName)
```

### C#

```csharp
System.bool ChangeRefConfigurationOfFlatPatternView(
   System.string ModelName,
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.bool ChangeRefConfigurationOfFlatPatternView(
   System.String^ ModelName,
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`: Name of the model in the flat-pattern view
- `ConfigName`: Name of the configuration

### Return Value

True if the configuration was successfully changed, false if not

## VBA Syntax

See [DrawingDoc::ChangeRefConfigurationOfFlatPatternView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ChangeRefConfigurationOfFlatPatternView.html).

## Remarks

Before calling this method, you must select the flat-pattern view of the model.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[DrawingDoc::CreateFlatPatternViewFromModelView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
