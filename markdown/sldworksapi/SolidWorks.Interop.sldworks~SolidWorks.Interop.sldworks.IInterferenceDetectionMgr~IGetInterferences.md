---
title: "IGetInterferences Method (IInterferenceDetectionMgr)"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr"
member: "IGetInterferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~IGetInterferences.html"
---

# IGetInterferences Method (IInterferenceDetectionMgr)

Calculates and gets the interferences.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetInterferences( _
   ByVal InterfernceCount As System.Integer _
) As Interference
```

### Visual Basic (Usage)

```vb
Dim instance As IInterferenceDetectionMgr
Dim InterfernceCount As System.Integer
Dim value As Interference

value = instance.IGetInterferences(InterfernceCount)
```

### C#

```csharp
Interference IGetInterferences(
   System.int InterfernceCount
)
```

### C++/CLI

```cpp
Interference^ IGetInterferences(
   System.int InterfernceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InterfernceCount`: Number of interferences

### Return Value

- in-process, unmanaged C++: Pointer to an array of [interferences](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterference.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IInterferenceDetectionMgr::GetInterferenceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IInterferenceDetectionMgr~GetInterferenceCount.html) to get the size of array for the interferences.

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[IInterferenceDetectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html)
[IInterferenceDetectionMgr::GetInterferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr~GetInterferences.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
