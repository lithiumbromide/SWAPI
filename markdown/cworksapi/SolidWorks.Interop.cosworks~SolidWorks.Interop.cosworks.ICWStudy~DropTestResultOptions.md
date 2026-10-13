---
title: "DropTestResultOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "DropTestResultOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestResultOptions.html"
---

# DropTestResultOptions Property (ICWStudy)

Gets the result options for this drop test study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DropTestResultOptions As CWDropTestResultOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWDropTestResultOptions

value = instance.DropTestResultOptions
```

### C#

```csharp
CWDropTestResultOptions DropTestResultOptions {get;}
```

### C++/CLI

```cpp
property CWDropTestResultOptions^ DropTestResultOptions {
   CWDropTestResultOptions^ get();
}
```

### Property Value

[ICWDropTestResultOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestResultOptions.html)

## VBA Syntax

See [CWStudy::DropTestResultOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~DropTestResultOptions.html).

## Examples

[Create Drop Test Study (VBA)](Create_Drop_Test_Study_Example_VB.htm)
[Create Drop Test Study (VB.NET)](Create_Drop_Test_Study_Example_VBNET.htm)
[Create Drop Test Study (C#)](Create_Drop_Test_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::AddDropTestSetup Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~AddDropTestSetup.html)
[ICWStudy::DropTestSetup Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestSetup.html)
[ICWStudy::DropTestStudyOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestStudyOptions.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
