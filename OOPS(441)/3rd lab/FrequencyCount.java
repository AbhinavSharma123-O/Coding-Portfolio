class FrequencyCount {
    public static void main(String[] args) {
        int[] arr = {2, 3, 2, 5, 3, 2, 5};
        for (int i = 0; i < arr.length; i++) {
            int count = 1;
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    count++;   
               }}
            System.out.println(arr[i] + " occurs " + count + " times");
        }}}
	