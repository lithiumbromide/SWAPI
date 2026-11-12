---
title: "ContactManager Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ContactManager"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ContactManager.html"
---

# ContactManager Property (ICWStudy)

Gets the contact manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ContactManager As CWContactManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWContactManager

value = instance.ContactManager
```

### C#

```csharp
CWContactManager ContactManager {get;}
```

### C++/CLI

```cpp
property CWContactManager^ ContactManager {
   CWContactManager^ get();
}
```

### Property Value

[Contact manager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager.html)

## VBA Syntax

See [CWStudy::ContactManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ContactManager.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::MultipleComponentContactsEditManager Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MultipleComponentContactsEditManager.html)
[ICWStudy::MultipleContactSetsEditManager Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~MultipleContactSetsEditManager.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
