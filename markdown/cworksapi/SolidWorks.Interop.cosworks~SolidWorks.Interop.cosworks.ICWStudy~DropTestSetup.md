---
title: "DropTestSetup Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "DropTestSetup"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestSetup.html"
---

# DropTestSetup Property (ICWStudy)

Gets the setup for this drop test study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DropTestSetup As CWDropTestSetup
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWDropTestSetup

value = instance.DropTestSetup
```

### C#

```csharp
CWDropTestSetup DropTestSetup {get;}
```

### C++/CLI

```cpp
property CWDropTestSetup^ DropTestSetup {
   CWDropTestSetup^ get();
}
```

### Property Value

[ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html)

## VBA Syntax

See [CWStudy::DropTestSetup](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~DropTestSetup.html).

## Examples

[Create Drop Test Study (C#)](Create_Drop_Test_Study_Example_CSharp.htm)
[Create Drop Test Study (VB.NET)](Create_Drop_Test_Study_Example_VBNET.htm)
[Create Drop Test Study (VBA)](Create_Drop_Test_Study_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::AddDropTestSetup Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~AddDropTestSetup.html)
[ICWStudy::DropTestResultOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestResultOptions.html)
[ICWStudy::DropTestStudyOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestStudyOptions.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
