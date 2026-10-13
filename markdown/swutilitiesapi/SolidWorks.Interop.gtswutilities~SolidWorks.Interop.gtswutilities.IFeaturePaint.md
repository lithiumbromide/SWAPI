---
title: "IFeaturePaint Interface"
project: "SOLIDWORKS Utilities API Help"
interface: "IFeaturePaint"
member: ""
kind: "interface"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFeaturePaint.html"
---

# IFeaturePaint Interface

Allows you to copy the feature parameters from one feature in a SOLIDWORKS part to a feature in a different SOLIDWORKS part.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IFeaturePaint
```

### Visual Basic (Usage)

```vb
Dim instance As IFeaturePaint
```

### C#

```csharp
public interface IFeaturePaint
```

### C++/CLI

```cpp
public interface class IFeaturePaint
```

## VBA Syntax

See [IFeaturePaint](ms-its:swutilitiesapivb6.chm::/swutilities~IFeaturePaint.html).

## Remarks

For example, you can specify a boss-extrude on one part and apply its parameters (such as depth) to another boss-extrude on a different part.

You can also specify two different features and apply feature parameters. For example, specify that a sweep feature apply its parameters (such as color and advanced color properties) to a dome feature.

## Accessors

[IUtilities::FeaturePaint](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.IUtilities~FeaturePaint.html)

## See Also

[IFeaturePaint Members](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.IFeaturePaint_members.html)
[SolidWorks.Interop.gtswutilities Namespace](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities_namespace.html)
