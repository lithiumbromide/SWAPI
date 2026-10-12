---
title: "BearingLoadBeginEdit Method (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "BearingLoadBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~BearingLoadBeginEdit.html"
---

# BearingLoadBeginEdit Method (ICWBearingLoad)

Starts editing a bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub BearingLoadBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad

instance.BearingLoadBeginEdit()
```

### C#

```csharp
void BearingLoadBeginEdit()
```

### C++/CLI

```cpp
void BearingLoadBeginEdit();
```

## VBA Syntax

See [CWBearingLoad::BearingLoadBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~BearingLoadBeginEdit.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

To start editing a bearing load, you must call this method. You must call [ICWBearingLoad::BearingLoadEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBearingLoad~BearingLoadEndEdit.html) to end editing that bearing load. Changes are not applied unless you call both methods.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
