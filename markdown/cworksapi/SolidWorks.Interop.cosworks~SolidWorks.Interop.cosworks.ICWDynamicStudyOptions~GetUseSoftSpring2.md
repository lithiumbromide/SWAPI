---
title: "GetUseSoftSpring2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetUseSoftSpring2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetUseSoftSpring2.html"
---

# GetUseSoftSpring2 Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetUseSoftSpring3](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetUseSoftSpring3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseSoftSpring2( _
   ByRef BUseSoftSpring As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BUseSoftSpring As System.Integer
Dim value As System.Integer

value = instance.GetUseSoftSpring2(BUseSoftSpring)
```

### C#

```csharp
System.int GetUseSoftSpring2(
   out System.int BUseSoftSpring
)
```

### C++/CLI

```cpp
System.int GetUseSoftSpring2(
   [Out] System.int BUseSoftSpring
)
```

### Parameters

- `BUseSoftSpring`: - 1 = Use soft spring to stabilize model
  - 0 = Do not use soft spring

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetUseSoftSpring2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetUseSoftSpring2.html).

## Remarks

You can use this method to check the stability of the model.

To stabilize the model for final runs, use:

- [ICWDynamicStudyOptions::SetUseSoftSpring2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetUseSoftSpring2.html) with BUseSoftSpring = 0.
- proper restraints.

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
