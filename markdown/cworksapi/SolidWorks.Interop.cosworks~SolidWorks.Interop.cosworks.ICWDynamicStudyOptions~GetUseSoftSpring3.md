---
title: "GetUseSoftSpring3 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetUseSoftSpring3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetUseSoftSpring3.html"
---

# GetUseSoftSpring3 Method (ICWDynamicStudyOptions)

Gets whether to use soft spring to stabilize the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseSoftSpring3( _
   ByRef BUseSoftSpring As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BUseSoftSpring As System.Boolean
Dim value As System.Integer

value = instance.GetUseSoftSpring3(BUseSoftSpring)
```

### C#

```csharp
System.int GetUseSoftSpring3(
   out System.bool BUseSoftSpring
)
```

### C++/CLI

```cpp
System.int GetUseSoftSpring3(
   [Out] System.bool BUseSoftSpring
)
```

### Parameters

- `BUseSoftSpring`: - -1 or true = Use soft spring to stabilize model
  - 0 or false = Do not use soft spring

### Return Value

0 indicates success; a non-0 value indicates failure

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
