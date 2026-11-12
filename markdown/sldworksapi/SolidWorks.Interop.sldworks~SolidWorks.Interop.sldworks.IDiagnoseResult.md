---
title: "IDiagnoseResult Interface"
project: "SOLIDWORKS API Help"
interface: "IDiagnoseResult"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.html"
---

# IDiagnoseResult Interface

Get the gaps and coedges in each gap on this body.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDiagnoseResult
```

### Visual Basic (Usage)

```vb
Dim instance As IDiagnoseResult
```

### C#

```csharp
public interface IDiagnoseResult
```

### C++/CLI

```cpp
public interface class IDiagnoseResult
```

## VBA Syntax

See [DiagnoseResult](ms-its:sldworksapivb6.chm::/sldworks~DiagnoseResult.html).

## Examples

[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

## Remarks

A gap is the laminar loop where the coedges on the loop do not have an associated face.

## Accessors

[IBody2::Diagnose](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Diagnose.html)

## Access Diagram

[DiagnoseResult](SWObjectModel.pdf#DiagnoseResult)

## See Also

[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeatureManager::InsertFillSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFillSurface2.html)
