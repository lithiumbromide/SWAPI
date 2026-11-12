---
title: "DropTestSetupEndEdit Method (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "DropTestSetupEndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~DropTestSetupEndEdit.html"
---

# DropTestSetupEndEdit Method (ICWDropTestSetup)

Ends editing the drop test setup.

## Syntax

### Visual Basic (Declaration)

```vb
Function DropTestSetupEndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Integer

value = instance.DropTestSetupEndEdit()
```

### C#

```csharp
System.int DropTestSetupEndEdit()
```

### C++/CLI

```cpp
System.int DropTestSetupEndEdit();
```

### Return Value

Error as defined in [swsDropTestSetUpError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDropTestSetUpError_e.html)

## VBA Syntax

See [CWDropTestSetup::DropTestSetupEndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~DropTestSetupEndEdit.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

You must call [ICWDropTestSetup::DropTestSetupBeginEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropTestSetupBeginEdit.html) to start editing a drop test setup. To end editing a drop test setup, you must call this method. Changes are not applied unless you call both methods.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
