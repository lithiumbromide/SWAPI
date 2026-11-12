---
title: "IGeneralTableFeature Interface"
project: "SOLIDWORKS API Help"
interface: "IGeneralTableFeature"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.html"
---

# IGeneralTableFeature Interface

Allows access to the general table feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IGeneralTableFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralTableFeature
```

### C#

```csharp
public interface IGeneralTableFeature
```

### C++/CLI

```cpp
public interface class IGeneralTableFeature
```

## VBA Syntax

See [GeneralTableFeature](ms-its:sldworksapivb6.chm::/sldworks~GeneralTableFeature.html).

## Examples

[Hide and Show Row (VBA)](Hide_and_Show_Row_Example_VB.htm)
[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

## Remarks

You can get this object using:

- [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) when a general table feature is selected in the FeatureManager design tree of the drawing.
- [ITableAnnotation::GeneralTableFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GeneralTableFeature.html).
- [IGeneralTableAnnotation::GeneralTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableAnnotation~GeneralTable.html).

The filename extension for a general table is .sldtbt. Table templates are not supplied for general tables.

## Accessors

See **Remarks**.

## Access Diagram

[GeneralTableFeature](SWObjectModel.pdf#GeneralTableFeature)

## See Also

[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IGeneralToleranceTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature.html)
