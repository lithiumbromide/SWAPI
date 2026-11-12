---
title: "Get Sketch Spline Parameters Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Sketch_Get_Spline_Parameters_Example_CPlusPlus_COM.htm"
---

# Get Sketch Spline Parameters Example (C++ COM)

This example shows how to get splines parameter data from sketches and how to unpack that data.

The method ISketch::IGetSplineParams2 returns an array, so this code must be used in an in-process DLL. Otherwise, use the method ISketch::GetSplineParams2 that returns a VARIANT.

```vb
// Union for use unpacking the data in the first two array elements for each spline
union SplinePackedData
{
 double doublevalue[2];
 int  intvalue[4];
};
void GetSketchSplines(LPSKETCH pSketch,CString* Message)
{
// Assume that pSketch has been set to a valid sketch already

 CString   Text;
 double*   pData;
 long   DataSize, NoSplines;

 // Get the spline parameters
 if(S_OK != pSketch->GetSplineParamsCount(&DataSize, &NoSplines) )return;

 if(NoSplines==0)
 {
  *Message += " Has no spline curves\r\n";
  return;
 }
 pData = (double*)malloc(sizeof(double) * DataSize);

 if(S_OK != pSketch->IGetSplineParams2(pData) )return;

 // Format the spline parameter data
 ExtractSplineData ( DataSize, pData, Message );

}

//////////////////////////////////////////////////////////////////////////
// Method: ExtractSplinesData
// Arguments: DataSize - Size of the array containing the splines parameters
//     pData - Data array containing splines parameters
// Return: Message - A CString for returning the formatted information
// Description:Extract the splines parameter data returned
//   from GetSplineParams and format it into a
//   string for display.
//////////////////////////////////////////////////////////////////////////
void CGetSketchesApp::ExtractSplinesData(int DataSize, double* pData, CString* Message)
{
 int     Index = 0;
 int     Dim;
 int     Order;
 int     nCtrlPoints;
 int     Periodic;
 int     nKnots;
 double    Knot;
 SplinePackedData* pPackedData;
 int     i,j;
 CString    Line;

// Continue until all the data is processed, i.e. 1 loop per spline
 while ( Index < DataSize )
 {
  // Unpack the information about the spline
  pPackedData = (SplinePackedData*)&pData[Index];
  Dim = pPackedData->intvalue[0];
  Order = pPackedData->intvalue[1];
  nCtrlPoints = pPackedData->intvalue[2];
  Periodic = pPackedData->intvalue[3];
  nKnots = Periodic ? nCtrlPoints+1 : nCtrlPoints+Order;

  // Format Text
  Line.Format(_T("Spline\r\nDimension %d\r\nNumControlPoints %d\r\n
Num of Knots %d\r\nPeriodic %d\r\n"),Dim, nCtrlPoints, nKnots, Periodic);

  *Message += Line;

  // Extract Control points
  Index+=2;
  // Step past packed data
  for ( i=0; i<nCtrlPoints; i++ )
  {
   // Assume 3 dimensions
   double CtrlPoint[3];

   for ( j=0; j<3; j++ )
   {
    CtrlPoint[j] = pData[Index++];
   }

   // Format text (in this case assume 3 dimensions)
   Line.Format(_T("Control Point: %lf %lf %lf\r\n"),
     CtrlPoint[0],
      CtrlPoint[1],
      CtrlPoint[2]);
   *Message += Line;
  }

  // Extract Knots
  for ( i=0; i<nKnots; i++ )
  {
   Knot = pData[Index++];

   // Format text
   Line.Format(_T("Knot: %lf\r\n"), Knot);
   *Message += Line;
  }
 }
}
```
