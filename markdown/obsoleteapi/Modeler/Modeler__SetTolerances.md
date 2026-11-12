---
title: "Modeler::SetTolerances"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Modeler/Modeler__SetTolerances.htm"
---

# Modeler::SetTolerances

This method is obsolete and has been superseded by [Modeler::GetToleranceValue](sldworksAPI.chm::/Modeler/Modeler__GetToleranceValue.htm) and [Modeler::SetToleranceValue](sldworksAPI.chm::/Modeler/Modeler__SetToleranceValue.htm).

Description

This method sets tolerances governing geometry output. These tolerance settings affect the precision of 2D and 3D trim curves that are approximated during output, such as UV trim curves or an intersection curve, which is represented by a Bspline. These settings do not affect curves that have an exact representation.

Syntax (OLE Automation)

Not Available.

Syntax (COM)

status = Modeler->SetTolerances ( ToleranceIDArray, ToleranceValueArray, NumTol, &retval )

| Input: | (long*) ToleranceIDArray | Array specifying the type of tolerance you want to set as defined in swTolerances_e |
| --- | --- | --- |
| Input: | (double*) ToleranceValueArray | Tolerance value in meters to assign for the particular ToleranceIDArray type |
| Input: | (long) NumTol | Number of tolerance types you are setting; this value should correspond to the number of elements in the ToleranceIDArray and ToleranceValueArray arrays |
| Output: | (VARIANT_BOOL) retval | TRUE if the tolerances is set successfully, FALSE if not |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The default tolerance setting for 3D geometry output is 0.01 meters, while 2D geometry uses a 1e-4 dimensionless tolerance value. If your 3D trim curves are coming out too far from the surfaces they are trimming or are not very close to the 2D trim curves, then you may want to tighten the tolerance. Set he tolerances before any extraction of geometry.

These tolerances can be reset by other add-ins, such as IGES, so make sure that they are set to your values when you need them. The tolerance settings only affect other add-in applications; however, you should be careful to reset the tolerances so that other add-in applications are not affected by your choice of tolerance. To reset the tolerances, use the Modeler::UnsetTolerances method.

The swUVCurveOutputTol tolerance is used during the extraction of UV (SP) trim curves. The Face2::GetTrimCurves2 method is affected by this setting. This tolerance value represents a fraction of the characteristic small dimension of a face (the tolerance is dimensionless). For example, if you set the swUVCurveOutputTol tolerance value to 3e-6, and the smallest dimension of the face is 0.4 meters, then the largest deviation of the trim curve will be:

(0.4 x 3e-6) meters

For reference, the SolidWorks IGES processor allows the user to control the swUVCurveOutputTol tolerance setting in the User Preferences area. The "Normal" setting under IGES uses a tolerance of 1e-4, while the "High" setting changes this tolerance to 3e-6. This IGES setting does not affect your application. Higher tolerance settings can increase processing time and the size of any output results.

As an example, if you set the tolerance for output of swBSCurveOutputTol and swBSCurveNonRationalOutputTol geometry types, then NumTol would equal 2 and ToleranceIDArray would be the following array:

[ swBSCurveOutputTol, swBSCurveNonRationalOutputTol ]

The ToleranceValueArray would be an array of tolerance values corresponding to the geometry types in ToleranceIDArray.

[ 0.001, 0.02 ]
