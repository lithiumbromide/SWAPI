---
title: "PressureBeginEdit Method (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "PressureBeginEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~PressureBeginEdit.html"
---

# PressureBeginEdit Method (ICWPressure)

Starts editing pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PressureBeginEdit()
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure

instance.PressureBeginEdit()
```

### C#

```csharp
void PressureBeginEdit()
```

### C++/CLI

```cpp
void PressureBeginEdit();
```

## VBA Syntax

See [CWPressure::PressureBeginEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~PressureBeginEdit.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## Remarks

To start editing pressure, you must call this method. You must call [ICWPressure::PressureEndEdit](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWPressure~PressureEndEdit.html) to end editing pressure. Changes are not applied unless you call both methods.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
