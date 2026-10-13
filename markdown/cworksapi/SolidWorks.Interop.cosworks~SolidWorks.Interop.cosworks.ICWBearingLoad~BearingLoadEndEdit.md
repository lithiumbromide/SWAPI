---
title: "BearingLoadEndEdit Method (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "BearingLoadEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~BearingLoadEndEdit.html"
---

# BearingLoadEndEdit Method (ICWBearingLoad)

Ends editing a bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Function BearingLoadEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Integer

value = instance.BearingLoadEndEdit()
```

### C#

```csharp
System.int BearingLoadEndEdit()
```

### C++/CLI

```cpp
System.int BearingLoadEndEdit();
```

### Return Value

Error as defined in [swsBearingLoadEndEditError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBearingLoadEndEditError_e.html)

## VBA Syntax

See [CWBearingLoad::BearingLoadEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~BearingLoadEndEdit.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

To start editing a bearing load, call [ICWBearingLoad::BearingLoadBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBearingLoad~BearingLoadBeginEdit.html). You must call ICWBearlingLoad::BearingLoadEndEdit to end editing a bearing load. Changes are not applied unless you call both methods.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
