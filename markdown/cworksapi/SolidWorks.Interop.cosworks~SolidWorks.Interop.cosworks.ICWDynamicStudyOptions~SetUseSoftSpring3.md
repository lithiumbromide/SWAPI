---
title: "SetUseSoftSpring3 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetUseSoftSpring3"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetUseSoftSpring3.html"
---

# SetUseSoftSpring3 Method (ICWDynamicStudyOptions)

Sets whether to use soft spring to stabilize the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUseSoftSpring3( _
   ByVal BUseSoftSpring As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BUseSoftSpring As System.Boolean
Dim value As System.Integer

value = instance.SetUseSoftSpring3(BUseSoftSpring)
```

### C#

```csharp
System.int SetUseSoftSpring3(
   System.bool BUseSoftSpring
)
```

### C++/CLI

```cpp
System.int SetUseSoftSpring3(
   System.bool BUseSoftSpring
)
```

### Parameters

- `BUseSoftSpring`: - -1 or true = Use soft spring to stabilize model
  - 0 or false = Do not use soft spring

### Return Value

0 indicates success; a non-0 value indicates failure

## Examples

See the [ICWDynamicStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html) examples.

## Remarks

Use [ICWDynamicStudyOptions::GetUseSoftSpring2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetUseSoftSpring2.html) to check the stability of the model.

To stabilize the model for final runs:

- set BUseSoftSpring = -1.
- use proper restraints.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
