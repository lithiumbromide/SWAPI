---
title: "DropTestSetupBeginEdit Method (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "DropTestSetupBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~DropTestSetupBeginEdit.html"
---

# DropTestSetupBeginEdit Method (ICWDropTestSetup)

Starts editing the drop test setup.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DropTestSetupBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup

instance.DropTestSetupBeginEdit()
```

### C#

```csharp
void DropTestSetupBeginEdit()
```

### C++/CLI

```cpp
void DropTestSetupBeginEdit();
```

## VBA Syntax

See [CWDropTestSetup::DropTestSetupBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~DropTestSetupBeginEdit.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

To start editing a drop test setup, you must call this method. You must call [ICWDropTestSetup::DropTestSetupEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropTestSetupEndEdit.html) to end editing a drop test setup. Changes are not applied unless you call both methods.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
