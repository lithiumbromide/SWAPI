---
title: "RemoveSaveBodies Method (ISaveBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData"
member: "RemoveSaveBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~RemoveSaveBodies.html"
---

# RemoveSaveBodies Method (ISaveBodyFeatureData)

Removes the specified bodies from this Save Bodies feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveSaveBodies( _
   ByVal Bodies As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveBodyFeatureData
Dim Bodies As System.Object
Dim value As System.Boolean

value = instance.RemoveSaveBodies(Bodies)
```

### C#

```csharp
System.bool RemoveSaveBodies(
   System.object Bodies
)
```

### C++/CLI

```cpp
System.bool RemoveSaveBodies(
   System.Object^ Bodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Bodies`: Array of bodies to remove from this Save Bodies feature

### Return Value

True if the bodies are removed from this Save Bodies feature, false if not

## VBA Syntax

See [SaveBodyFeatureData::RemoveSaveBodies](ms-its:sldworksapivb6.chm::/sldworks~SaveBodyFeatureData~RemoveSaveBodies.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html)
[ISaveBodyFeatureData::AddSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~AddSaveBodies.html)
[ISaveBodyFeatureData::GetSaveBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~GetSaveBodies.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
