---
title: "Close Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "Close"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~Close.html"
---

# Close Method (gtcocswPowerSelect)

Closes the current session of PowerSelect.

## Syntax

### Visual Basic (Declaration)

```vb
Function Close() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim value As System.Integer

value = instance.Close()
```

### C#

```csharp
System.int Close()
```

### C++/CLI

```cpp
System.int Close();
```

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::Close](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~Close.html).

## Remarks

Because you cannot have more than one SOLIDWORKS Utilities tool running at any one time, you must close a running PowerSelect session before you can use another SOLIDWORKS Utilities tool. To initialize a PowerSelect session, call [IPowerSelect::Init](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~Init.html).

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
