---
title: "ForceMisalignment Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "ForceMisalignment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~ForceMisalignment.html"
---

# ForceMisalignment Method (IMate2)

Forces a misaligned mate condition for this concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function ForceMisalignment() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

value = instance.ForceMisalignment()
```

### C#

```csharp
System.bool ForceMisalignment()
```

### C++/CLI

```cpp
System.bool ForceMisalignment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the misaligned mate condition is successfully created, false if not

## VBA Syntax

See [Mate2::ForceMisalignment](ms-its:sldworksapivb6.chm::/sldworks~Mate2~ForceMisalignment.html).

## Examples

```
'VBA
```

```
' Open an assembly with a misaligned concentric mate, Concentric1
```

```
Dim swfeature As SldWorks.Feature
Dim swmate As SldWorks.Mate2
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swassm = swApp.ActiveDoc
    Set Swfeat = swassm.FeatureByName("Concentric1")
    Set swmate = Swfeat.GetSpecificFeature2
    Debug.Print "Concentric mate type as defined in swConcentricAlignmentType_e: " & swmate.GetConcentricAlignmentType
```

```
    'Remove the misaligned mate condition
    swmate.RemoveMisalignment
```

```
    'Create the misaligned mate condition
    swmate.ForceMisalignment
```

```
End Sub
```

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::RemoveMisalignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~RemoveMisalignment.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
