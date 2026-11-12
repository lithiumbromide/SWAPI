---
title: "RadiationBeginEdit Method (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "RadiationBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~RadiationBeginEdit.html"
---

# RadiationBeginEdit Method (ICWRadiation)

Starts editing radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RadiationBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation

instance.RadiationBeginEdit()
```

### C#

```csharp
void RadiationBeginEdit()
```

### C++/CLI

```cpp
void RadiationBeginEdit();
```

## VBA Syntax

See [CWRadiation::RadiationBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~RadiationBeginEdit.html).

## Examples

See the [ICWRadiation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html) examples.

## Remarks

To start editing radiation, you must call this method. You must call [ICWRadiation::RadiationEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWRadiation~RadiationEndEdit.html) to end editing radiation. Changes are not applied unless you call both methods.

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
