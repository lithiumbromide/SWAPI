---
title: "LoadsAndRestraintsManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "LoadsAndRestraintsManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~LoadsAndRestraintsManager.html"
---

# LoadsAndRestraintsManager Property (ICWStudy)

Gets the loads and restraints manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property LoadsAndRestraintsManager As CWLoadsAndRestraintsManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWLoadsAndRestraintsManager

value = instance.LoadsAndRestraintsManager
```

### C#

```csharp
CWLoadsAndRestraintsManager LoadsAndRestraintsManager {get;}
```

### C++/CLI

```cpp
property CWLoadsAndRestraintsManager^ LoadsAndRestraintsManager {
   CWLoadsAndRestraintsManager^ get();
}
```

### Property Value

[Loads and restraints manager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager.html)

## VBA Syntax

See [CWStudy::LoadsAndRestraintsManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~LoadsAndRestraintsManager.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
