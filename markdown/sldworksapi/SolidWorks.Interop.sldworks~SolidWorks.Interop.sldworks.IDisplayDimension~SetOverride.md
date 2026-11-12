---
title: "SetOverride Method (IDisplayDimension)"
project: "SOLIDWORKS API Help"
interface: "IDisplayDimension"
member: "SetOverride"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetOverride.html"
---

# SetOverride Method (IDisplayDimension)

Sets whether to display the actual dimension value or to display another value, and, if so, that value.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverride( _
   ByVal Override As System.Boolean, _
   ByVal Value As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayDimension
Dim Override As System.Boolean
Dim Value As System.Double
Dim value As System.Boolean

value = instance.SetOverride(Override, Value)
```

### C#

```csharp
System.bool SetOverride(
   System.bool Override,
   System.double Value
)
```

### C++/CLI

```cpp
System.bool SetOverride(
   System.bool Override,
   System.double Value
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Override`: True to display a value other than the actual dimension value, false to display the actual value
- `Value`: Value to display instead of the actual dimension value

### Return Value

True if setting an override value is successful, false if not

## VBA Syntax

See [DisplayDimension::SetOverride](ms-its:sldworksapivb6.chm::/sldworks~DisplayDimension~SetOverride.html).

## Remarks

This method can only be used on a display dimension in a drawing. In a part or assembly, this method takes no action and returns false.

If Override is set to false, then the Value argument is ignored.

Use [IDisplayDimension::GetOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetOverride.html) to get whether the actual dimension value or another value is displayed.

Use [IDisplayDimension::GetOverrideValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension~GetOverrideValue.html) to get the value to display instead of the actual dimension value.

## See Also

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.html)
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html)
