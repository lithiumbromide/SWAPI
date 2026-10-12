---
title: "RemoveMisalignment Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "RemoveMisalignment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~RemoveMisalignment.html"
---

# RemoveMisalignment Method (IMate2)

Removes the misaligned mate condition of this concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMisalignment() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim value As System.Boolean

value = instance.RemoveMisalignment()
```

### C#

```csharp
System.bool RemoveMisalignment()
```

### C++/CLI

```cpp
System.bool RemoveMisalignment();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the misaligned mate condition is successfully removed, false if not

## VBA Syntax

See [Mate2::RemoveMisalignment](ms-its:sldworksapivb6.chm::/sldworks~Mate2~RemoveMisalignment.html).

## Examples

```
'VBA
```

```
'Open an assembly with a misaligned concentric mate, Concentric1
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

## Remarks

After calling this method, one of the concentric mates may be unsolvable.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::ForceMisalignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~ForceMisalignment.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
