---
title: "CreateFlatPatternViewFromModelView2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateFlatPatternViewFromModelView2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView2.html"
---

# CreateFlatPatternViewFromModelView2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateFlatPatternViewFromModelView3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateFlatPatternViewFromModelView3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateFlatPatternViewFromModelView2( _
   ByVal ModelName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal LocX As System.Double, _
   ByVal LocY As System.Double, _
   ByVal LocZ As System.Double, _
   ByVal HideBendLines As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim ConfigName As System.String
Dim LocX As System.Double
Dim LocY As System.Double
Dim LocZ As System.Double
Dim HideBendLines As System.Boolean
Dim value As System.Boolean

value = instance.CreateFlatPatternViewFromModelView2(ModelName, ConfigName, LocX, LocY, LocZ, HideBendLines)
```

### C#

```csharp
System.bool CreateFlatPatternViewFromModelView2(
   System.string ModelName,
   System.string ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.bool HideBendLines
)
```

### C++/CLI

```cpp
System.bool CreateFlatPatternViewFromModelView2(
   System.String^ ModelName,
   System.String^ ConfigName,
   System.double LocX,
   System.double LocY,
   System.double LocZ,
   System.bool HideBendLines
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`: Name of model
- `ConfigName`: Name of configuration
- `LocX`: X coordinate
- `LocY`: Y coordinate
- `LocZ`: Z coordinate
- `HideBendLines`: True hides bend lines, false does not

### Return Value

True if the flat-pattern view was created successfully, false if it was not

## VBA Syntax

See [DrawingDoc::CreateFlatPatternViewFromModelView2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateFlatPatternViewFromModelView2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ChangeRefConfigurationOfFlatPatternView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ChangeRefConfigurationOfFlatPatternView.html)
[IDrawingDoc::CreateDrawViewFromModelView3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDrawViewFromModelView3.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
