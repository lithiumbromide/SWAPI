---
title: "IGeneralToleranceTableFeature Interface"
project: "SOLIDWORKS API Help"
interface: "IGeneralToleranceTableFeature"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature.html"
---

# IGeneralToleranceTableFeature Interface

Allows access to the general tolerance table feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IGeneralToleranceTableFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralToleranceTableFeature
```

### C#

```csharp
public interface IGeneralToleranceTableFeature
```

### C++/CLI

```cpp
public interface class IGeneralToleranceTableFeature
```

## VBA Syntax

See [GeneralToleranceTableFeature](ms-its:sldworksapivb6.chm::/sldworks~GeneralToleranceTableFeature.html).

## Examples

[Insert General Tolerance Table (VBA)](Insert_General_Tolerance_Table_Example_VB.htm)
[Insert General Tolerance Table (VB.NET)](Insert_General_Tolerance_Table_Example_VBNET.htm)
[Insert General Tolerance Table (C#)](Insert_General_Tolerance_Table_Example_CSharp.htm)

## Remarks

You can access this object by calling:

- [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) after selecting a general tolerance table feature in the Tables folder of the FeatureManager design tree

- or -

- [IGeneralToleranceTableAnnotation::GeneralToleranceTableFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableAnnotation~GeneralToleranceTableFeature.html)

## Accessors

See **Remarks**.

## Access Diagram

[GeneralToleranceTableFeature](SWObjectModel.pdf#GeneralToleranceTableFeature)

## See Also

[IGeneralToleranceTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IGeneralTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.html)
[IModelDocExtension::InsertGeneralToleranceTableAnnotation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralToleranceTableAnnotation.html)
