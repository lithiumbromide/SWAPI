---
title: "Initialize Method (IMateControllerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMateControllerFeatureData"
member: "Initialize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize.html"
---

# Initialize Method (IMateControllerFeatureData)

Initializes this mate controller with the specified mates.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Initialize( _
   ByVal Mates As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMateControllerFeatureData
Dim Mates As System.Object

instance.Initialize(Mates)
```

### C#

```csharp
void Initialize(
   System.object Mates
)
```

### C++/CLI

```cpp
void Initialize(
   System.Object^ Mates
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mates`: Array of supportive [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)

## VBA Syntax

See [MateControllerFeatureData::Initialize](ms-its:sldworksapivb6.chm::/sldworks~MateControllerFeatureData~Initialize.html).

## Examples

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html) examples.

## Remarks

Before calling this method, use [IAssemblyDoc::IsSupportedMatesAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsSupportedMatesAvailable.html) and [IAssemblyDoc::CollectAllSupportiveMates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates.html) to determine appropriates mates with which to initialize this mate controller.

Mates passed to this method are given precedence over pre-selected mates. If this method is not called or invalid mates are passed to it, then pre-selected mates are used.

For .NET applications, you must marshal the Mates array to IDispatch object arrays before calling this method. See [IDispatch Object Arrays as Input in .NET](ms-its:sldworksapiprogguide.chm::/Overview/IDispatch_Object_Arrays_as_Input_in_.NET.htm).

## See Also

[IMateControllerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html)
[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
