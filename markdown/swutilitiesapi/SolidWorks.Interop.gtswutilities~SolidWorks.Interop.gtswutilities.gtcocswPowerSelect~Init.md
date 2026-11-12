---
title: "Init Method (gtcocswPowerSelect)"
project: "SOLIDWORKS Utilities API Help"
interface: "gtcocswPowerSelect"
member: "Init"
kind: "method"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect~Init.html"
---

# Init Method (gtcocswPowerSelect)

Initializes a session of PowerSelect.

## Syntax

### Visual Basic (Declaration)

```vb
Function Init() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As gtcocswPowerSelect
Dim value As System.Integer

value = instance.Init()
```

### C#

```csharp
System.int Init()
```

### C++/CLI

```cpp
System.int Init();
```

### Return Value

Error as defined in [gtError_e](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.gtError_e.html)

## VBA Syntax

See [IPowerSelect::Init](ms-its:swutilitiesapivb6.chm::/swutilities~IPowerSelect~Init.html).

## Remarks

This method binds the currently active document to PowerSelect. All PowerSelect API-related calls between IPowerSelect::Init and [IPowerSelect::Close](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IPowerSelect~Close.html) work on this document. SOLIDWORKS Utilities API calls that try to activate other documents will fail.

You cannot have more than one SOLIDWORKS Utilities tool running at any one time. You must close a running PowerSelect session before you can use another SOLIDWORKS Utilities tool.

An error message is returned if a session of PowerSelect is already running when IPowerSelect::Init is called, either programmatically or in the user interface.

## See Also

[gtcocswPowerSelect Interface](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect.html)
[gtcocswPowerSelect Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtcocswPowerSelect_members.html)

## Availability

SOLIDWORKS Utilities API 2005 FCS
