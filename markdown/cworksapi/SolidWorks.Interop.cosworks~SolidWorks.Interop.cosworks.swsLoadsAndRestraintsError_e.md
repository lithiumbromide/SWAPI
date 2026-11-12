---
title: "swsLoadsAndRestraintsError_e Enumeration"
project: "SOLIDWORKS Simulation API Help"
interface: "swsLoadsAndRestraintsError_e"
member: ""
kind: "enum"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLoadsAndRestraintsError_e.html"
---

# swsLoadsAndRestraintsError_e Enumeration

Loads and restraints errors

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swsLoadsAndRestraintsError_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swsLoadsAndRestraintsError_e
```

### C#

```csharp
public enum swsLoadsAndRestraintsError_e : System.Enum
```

### C++/CLI

```cpp
public enum class swsLoadsAndRestraintsError_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swsLoadsAndRestraintsError_InvalidComponentsCount | 3 = Number of bodies/components must be greater than one |
| swsLoadsAndRestraintsError_InvalidLicense | 7 = Not available with current license |
| swsLoadsAndRestraintsError_InvalidOrNullFace | 6 = Invalid or null face input |
| swsLoadsAndRestraintsError_InvalidSelection | 4 = Wrong object has been passed |
| swsLoadsAndRestraintsError_InvalidSelectionsMixedTogether | 5 = Non-supported entities selected together |
| swsLoadsAndRestraintsError_NoLBCDefined | 8 = No load or restraint defined |
| swsLoadsAndRestraintsError_NotFoundWithGivenName | 2 = Load or restraint with specified name not found |
| swsLoadsAndRestraintsErrorNotFoundAtIndex | 1 = Load or restraint not found at this index |
| swsLoadsAndRestraintsErrorSuccessful | 0 = Successful |

## See Also

[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
